#!/usr/bin/env python3
"""Class BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching
from typing import Any, Optional


class BasicCache(BaseCaching):
    def __init__(self):
        """
        Initialize the object.
        """
        super().__init__()

    def put(self, key: Any, item: Any) -> None:
        """
        Adds an item to the cache.

        Args:
            key (Any): The key to associate with the item.
            item (Any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Any]:
        """
        Get the value associated with the given key from the cache.

        Parameters:
            key (Any): The key to search for in the cache.

        Returns:
            Any: The value associated with the given key, or None if the key
            is None or not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
