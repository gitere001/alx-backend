#!/usr/bin/env python3
"""Class BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from typing import Any, Optional


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching"""
    def __init__(self) -> None:
        """
        Initialize the object.
        """
        super().__init__()
        self.order = []

    def put(self, key: Any, item: Any) -> None:
        """
        put - Adds an item in the cache.
        uses first in first out (FIFO) to evict the least recently used item
        """
        if key is None or item is None:
            return
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            first_key = self.order.pop(0)
            print("DISCARD: {}".format(first_key))
            del self.cache_data[first_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key: Any) -> Optional[Any]:
        """
        get - Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
