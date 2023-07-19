#!/usr/bin/env python3
"""
"""
import sys
import random
from typing import Union, Optional, Callable
from uuid import uuid4

import redis

ManyTypes = Union[str, bytes, int, float]

class Cache:
    """
    creating a cache to store something
    """

    def __init__(self):
        """
        constructor that calls the redis
        the flash the instance
        """
        self._redis = redis.Redis
        self._redis.flushdb

    @count_calls
    @call_history
    def store(self, data: ManyTypes) -> str:
        """
        method that generates a random key
        for the UUID
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> ManyTypes:
        """
        converts data to the desired
        format
        """
        if fn :
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data
    
    def get_str(self: bytes) -> str:
        """
        gets the input user data str
        """
        return self.decode("utf-8")
    
    def get_int(self: bytes) -> int:
        """
        gets the input int ID
        """
        return int.from_bytes(self, sys.byteorder)
