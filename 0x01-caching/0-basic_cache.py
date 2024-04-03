#!/usr/bin/python3
""" 0. Basic dictionary """


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and implements a basic ict cache. """

    def put(self, key, item):
        """Assign key and item to the cache system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get the value from the cache with key """
        return self.cache_data.get(key, None)