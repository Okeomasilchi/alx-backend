#!/usr/bin/env python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class likely represents a basic
    caching mechanism in Python.
    """

    def __init__(self):
        """Call the constructor of the parent class"""
        super().__init__()

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
