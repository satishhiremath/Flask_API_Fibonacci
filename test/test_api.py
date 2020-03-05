import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parent_dir)
os.sys.path.insert(0, os.path.join(parent_dir, 'src'))

from src.api import FlaskAPI
from src.api import *
from src.logger import Logger
from src.fibonacci_seq_calculator import FibSeqCalculator


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.logger_obj = Logger()
        logger = self.logger_obj.create_logger(__name__)
        flask_obj = FlaskAPI(logger)
        self.fib_seq_calc = FibSeqCalculator(logger)

    def test_get_fib(self):
        target = 5
        out = self.fib_seq_calc.get_fib(target)
        self.assertEqual(out, 8)

    def test_sum_of_combinations(self):
        target = 11
        self.fib_seq_calc.calculate(target)
        fib_combinations = self.fib_seq_calc.get_result(target)
        sum_not_equals_target = False
        for combination in fib_combinations:
            if sum(combination) != target:
                sum_not_equals_target = True
        self.assertEqual(sum_not_equals_target, False)

    def test_get_fibonacci_numbers(self):
        number = 11
        seq = self.fib_seq_calc.get_fibonacci_numbers(number)
        result = [2, 3, 5, 8]
        self.assertEqual(result, seq)


if __name__ == '__main__':
    unittest.main()
