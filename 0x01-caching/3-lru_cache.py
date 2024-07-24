#!/usr/bin/env python3
"""Class BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from typing import Any


class LRUCache(BaseCaching):
    def __init__(self) -> None:
        """
        Initialize the object.
        """
        super().__init__()
        self.order = []

    def put(self, key: Any, item: Any) -> None:
        if key is None or item is None:
            return
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """
        Get the value associated with the given key from the cache.

        Parameters:
            key (Any): The key to search for in the cache.

        Returns:
            Any: The value associated with the given key, or None if the key
            is None or not found in the cache.

        This method removes the key from the current position in the order list
        and appends it to the end of the order list. It then returns the value
        associated with the key from the cache data.
        """

        if key is None or key not in self.cache_data:
            return None
        del self.order[self.order.index(key)]
        self.order.append(key)
        return self.cache_data[key]
