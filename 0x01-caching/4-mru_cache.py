#!/usr/bin/env python3
"""Class MRUCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from typing import Any


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching"""
    def __init__(self) -> None:
        """Initialize the object"""
        super().__init__()
        self.order = []

    def put(self, key: Any, item: Any) -> None:
        """a method put - Adds an item in the cache"""
        if key is None or item is None:
            return
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self: Any, key: Any) -> Any:
        """a method get - Returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        del self.order[self.order.index(key)]
        self.order.append(key)
        return self.cache_data[key]
