#!/usr/bin/env python3
""""""
from base_caching import BaseCaching
from typing import Any


class LIFOCache(BaseCaching):
    def __init__(self) -> None:
        super().__init__()
        self.order = []

    def put(self, key: Any, item: Any) -> Any:
        if key is None or item is None:
            return
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(F"DISCARD: {self.order[-1]}")
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """
        get - Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
