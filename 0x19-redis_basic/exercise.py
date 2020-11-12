#!/usr/bin/env python3
"""exercise.py"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from sys import byteorder
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Counts number of calls to a class method """
    # use qualname dunder for qualified class method name
    key = method.__qualname__
    # use functools.wraps to create wrapper method for incrementing

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """store called func in redis list"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper func"""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """prints the data"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    in_list = redis.lrange(inputs, 0, -1)
    out_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(in_list, out_list))
    for a, b in redis_zipped:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """ Class for methods that operate a caching system """

    def __init__(self):
        """ Instance of Redis db """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Creates key and stores it with data """
        # uuid must be type cast to str for Redis to be able to accept it
        key = str(uuid4())
        # use pipelining for multi sets, mset() is not approrpiate for a cache
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """ Returns data converted to desired format """
        # default Redis.get in case key does not exist
        data = self._redis.get(key)
        # use callable if one provided
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """ Convert bytes to str """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Convert bytes to int """
        return int.from_bytes(data, byteorder)
