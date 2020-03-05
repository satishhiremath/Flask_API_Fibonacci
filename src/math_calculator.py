'''
This is Base class for future math calculators
At present only FibSeqCalculator class inherits this class
'''

from typing import List


class MathCalculator:
    def __init__(self):
        pass

    def _calculate(self, num: int):
        raise NotImplementedError()

    def _get_result(self, num: int) -> List:
        raise NotImplementedError()
