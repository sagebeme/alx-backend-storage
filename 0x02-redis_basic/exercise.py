#!/usr/bin/env python3
"""
"""
import random
from typing import Union, Optional, Callable
from uuid import uuid4

import redis


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
    def store(self, data: UnionOfTypes) -> str:
        """
        method that generates a random key
        for the UUID
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
