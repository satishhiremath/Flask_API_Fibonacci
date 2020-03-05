import os
import json
from typing import List, Dict
import logging


class ResultsCache:
    def __init__(self):
        if os.path.isfile("./cache.json"):
            with open("./cache.json", 'r') as json_file:
                self.__cache_data = json.load(json_file)
        else:
            self.__cache_data = {}

    def dump_cache(self):
        """Dumps cache data back to json file"""
        with open("./cache.json", 'w') as outfile:
            json.dump(self.__cache_data, outfile)

    def add_result(self, num: int, value: List):
        """Adds result to cache"""
        if str(num) not in self.__cache_data.keys():
            self.__cache_data[num] = value

    def get_cache(self) -> Dict:
        """Returns cache data"""
        return self.__cache_data
