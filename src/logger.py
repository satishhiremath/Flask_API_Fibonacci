'''
This class deals with logging to File and terminal
'''

import sys
import logging


class Logger:
    def __init__(self):
        self.__api_log_file = "api.log"

    def create_logger(self, name: str):
        """Creates logger object with given name and log level"""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        f_handler = self.__get_file_handler(filename=self.__api_log_file)
        s_handler = self.__get_stream_handler()
        logger.addHandler(f_handler)
        logger.addHandler(s_handler)
        return logger

    def __get_file_handler(self, filename: str):
        """Returns file handler for logging"""
        f_handler = logging.FileHandler(filename=filename)
        f_handler.setLevel(logging.DEBUG)
        return f_handler

    def __get_stream_handler(self):
        """Returns stream handler for logging"""
        s_handler = logging.StreamHandler(sys.stdout)
        s_handler.setLevel(logging.DEBUG)
        return s_handler
