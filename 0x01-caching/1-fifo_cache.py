#!/usr/bin/env python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class likely represents a basic
    caching mechanism in Python.
    """
    def __init__(self):
        """Call the constructor of the parent class"""
        super().__init__()
        self.vals = []

    def put(self, key: str, item: str) -> None:
        """
        Add an item to the cache.

        Args:
          key (str): The key to associate with
            the item.
          item (any): The item to be stored in
            the cache.

        Returns:
          None
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS and self.vals:
                self.cache_data.pop(self.vals[0], None)
                print(f"DISCARD: {self.vals[0]}")
                # print(self.vals[0])
                del self.vals[0]
            self.vals.append(key)
            # print(self.vals)
            self.cache_data[key] = item

    def get(self, key: str) -> dict:
        """
        Retrieve the value associated with the given
        key from the cache.

        Args:
          key (str): The key to retrieve the value for.

        Returns:
          dict: The value associated with the key, or
            None if the key is not found in the cache.
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
