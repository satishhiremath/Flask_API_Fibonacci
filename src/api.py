'''
This class creates Flask Api
'''

import requests
import functools
from time import strftime
from flask import Flask, request
from healthcheck import HealthCheck

from logger import Logger
from service_profiler import ServiceProfiler
from fibonacci_seq_calculator import FibSeqCalculator as FibSeqCal

HOST_URL = "0.0.0.0"
PORT = "5000"
API_URL = "http://" + HOST_URL + ":" + PORT + "/fib/"


class FlaskAPI:
    def __init__(self, logger_inst):
        self.logger = logger_inst
        self.app = self.create_app()

    def create_app(self) -> Flask:
        """Creates and returns Flask app"""
        return Flask(__name__)

    @ServiceProfiler.profile
    def run_app(self):
        self.logger.info("Running Flask API on host:{}".format(HOST_URL))
        self.app.run(debug=True, host=HOST_URL)

    @ServiceProfiler.profile
    def test_api_health(self):
        try:
            response = requests.get(API_URL, timeout=3)
            print(response.status_code)
            print(response.text)
            response.raise_for_status()
        except requests.exceptions.HTTPError as httpErr:
            self.logger.info("Http Error:", httpErr)
        except requests.exceptions.ConnectionError as connErr:
            self.logger.info("Error Connecting:", connErr)
        except requests.exceptions.Timeout as timeOutErr:
            self.logger.info("Timeout Error:", timeOutErr)
        except requests.exceptions.RequestException as reqErr:
            self.logger.info("Something Else:", reqErr)
        return True, "http OK"


if __name__ == "__main__":
    logger_obj = Logger()
    logger = logger_obj.create_logger(__name__)

    flask_api_obj = FlaskAPI(logger)

    health = HealthCheck()
    health.add_check(flask_api_obj.test_api_health)


    @ServiceProfiler.profile
    @flask_api_obj.app.route('/', methods=['GET'])
    @flask_api_obj.app.route('/home', methods=['GET'])
    def hello():
        return "Welcome to Adnymics task home page. APIs implemented [/health], [/fib/number]"


    @ServiceProfiler.profile
    @flask_api_obj.app.route('/fib/<int:number>', methods=['GET'])
    @functools.lru_cache(maxsize=None)
    def fib_combinations(number):
        fib_sec_calc = FibSeqCal(logger)
        fib_sec_calc.calculate(number)
        output = fib_sec_calc.get_result(number)
        return str(output)


    @ServiceProfiler.profile
    @flask_api_obj.app.after_request
    def after_request(response):
        timestamp = strftime('[%Y-%b-%d %H:%M]')
        logger.error('Timestamp=%s Addr=%s Method=%s Scheme=%s Path=%s Status=%s', timestamp, request.remote_addr,
                     request.method, request.scheme, request.full_path, response.status)
        return response

    flask_api_obj.app.add_url_rule("/health", "health", view_func=lambda: health.run())

    flask_api_obj.run_app()
