'''
This Class inherits from  base class MathCalculator
It Computes Fibonacci sequence sum combinations of a number
'''

import functools
from typing import List
from itertools import combinations_with_replacement

from math_calculator import MathCalculator
from service_profiler import ServiceProfiler
from result_cache import ResultsCache


class FibSeqCalculator(MathCalculator):
    def __init__(self, logger):
        self.__logger = logger
        self.__target = 0
        self.__possible_arrays = []
        self.__combinations = []
        self.cache_obj = ResultsCache()
        self.get_fib.cache_clear()

    def __del__(self):
        pass

    @functools.lru_cache(maxsize=None)
    def get_fib(self, num: int):
        """Returns fibonacci of a number"""
        if num == 2:
            return 2
        if num <= 1:
            return 1
        value = self.get_fib(num - 2) + self.get_fib(num - 1)
        return value

    def get_fibonacci_numbers(self, num: int) -> List:
        """Returns fibonacci numbers until num"""
        if num < 2:
            self.__logger.error("Provide values greater than or equal to 2")
        cache = self.cache_obj.get_cache()

        if str(num) in cache.keys():
            return cache[str(num)]

        n_list = [int(i) for i in cache.keys() if int(i) < num]
        fib_sequence = list()
        n = 2
        if n_list:
            fib_sequence.extend(cache[str(max(n_list))])
            n = len(cache[str(max(n_list))]) + 2
        fib = 0

        while fib < num:
            fib = self.get_fib(n)
            if fib < num:
                fib_sequence.append(fib)
            n += 1
        self.cache_obj.add_result(num, fib_sequence)
        return fib_sequence

    def get_combinations(self, fib_list: List):
        """Returns possible combinations"""
        if len(fib_list) > 0:
            for value in range(0, fib_list[-1]):
                possible_pair = list(combinations_with_replacement(fib_list, value))
                self.__possible_arrays += possible_pair

            for item in self.__possible_arrays:
                if sum(item) == self.__target:
                    self.__combinations.append(list(item))

    @ServiceProfiler.profile
    def calculate(self, num: int):
        """Calculates possible combinations"""
        self.__combinations.clear()
        self.__target = num
        fib_list = self.get_fibonacci_numbers(self.__target)
        self.__logger.info("Cache Info: {}".format(self.get_fib.cache_info()))
        self.get_combinations(fib_list)

    def get_result(self, num: int) -> List:
        """Returns list of combinations"""
        self.__logger.info("Fibonacci combinations for num: {} is {}".format(num, self.__combinations))
        self.cache_obj.dump_cache()
        return self.__combinations
