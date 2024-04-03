#!/usr/bin/env python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    This class likely represents a basic
    caching mechanism in Python.
    """

    MAX_ITEMS = float("inf")

    def __init__(self):
        """Call the constructor of the parent class"""
        super().__init__()

    def put(self, key: str, item: any) -> None:
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
        if [key, item] is None:
            pass
        else:
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
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
