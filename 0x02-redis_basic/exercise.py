#!/usr/bin/env python3
"""
This module contains a class Cache that implements
a simple cache using Redis
"""
import redis
import uuid
from typing import Any, Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator function that records the number of times
    the function has been called in a cache

    Args:
        method - wrapped function

    Return:
        wrapper function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    decorations function that keeps a record of the call
    history of a method, including outputs and inputs

    Args:
        method: decorated function

    Return:
        Callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper



def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function

    Args:
        method (callable: The function whose history of calls
        is to be displayed.

    Returns:
        None
    """
    redis_client = getattr(method.__self__, '_redis', None)
    qual_name = method.__qualname__
    input_key = "{}:inputs".format(qual_name)
    output_key = "{}:outputs".format(qual_name)
    call_count = 0

    if redis_client.exists(qual_name):
        call_count = int(redis_client.get(qual_name))
    print("{} was called {} times:".format(qual_name, call_count))

    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)
    for _input, _output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
                qual_name,
                _input.decode('utf-8'),
                _output.decode('utf-8')
            ))
    

class Cache:
    """
    simple implementation of a cache 
    
    Attributes:
        _redis: private class atribute that stores a redis Client
    """
    def __init__(self):
        """
        class constructor, initailizes the class

        Args:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        saves data to the cache

        Args:
            data(str, int, float, bytes): data to store

        Return:
            key of the stored data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes],\
            Union[str, bytes, int, float]]]=None) -> Union[str, bytes, int, float, None]:
        """
        fetches and returns data in cache based on key

        Args:
            key(str): key for the data
            fn(Callable): function to convert byte data to desired form

        Return:
            retrived[converted] data
        """
        data = self._redis.get(key)
        if not data:
            return None
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """
        converts data to an string

        Args:
            data(bytes): data in bytes from redis

        Return:
            string value of data
        """
        return self.get(data, lambda d: d.decode('utf-8'))

    def get_int(self, data: bytes) -> int:
        """
        converts data to a integer

        Args:
            data(bytes): data in bytes from redis

        Return:
            integer value of data
        """
        return self.get(data, lambda d: int(d))


cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
