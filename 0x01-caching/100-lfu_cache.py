#!/usr/bin/env python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.freq = defaultdict(int)

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            LFU = min(self.freq.values())
            keys_least_freq = [
              k for k, v in self.freq.items()
              if v == LFU
              ]

            if len(keys_least_freq) == 1:
                _key = keys_least_freq[0]
            else:
                lru_key = min(self.cache_data, key=self.freq.get)
                _key = lru_key

            del self.cache_data[_key]
            del self.freq[_key]
            print("DISCARD:", _key)

        self.cache_data[key] = item
        self.freq[key] += 1

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        return self.cache_data[key]
