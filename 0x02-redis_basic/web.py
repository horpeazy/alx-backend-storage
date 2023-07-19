#!/usr/bin/env python3
""" 
This module contains a function that uses the requests module
to obtain the HTML content of a particular URL and returns it.
It also contains a wrraper function that  tracks how many times
a particular URL was accessed in the key "count:{url}" and cache
the result with an expiration time of 10 seconds.
"""
import redis
import requests
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def cache_result(fn: Callable) -> Callable:
    """
    decorator function to cache url

    Args:
        fn (callable): decorated function

    Return:
        wrapper function
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """ wrapper function """
        url = args[0]
        count_key = "count:{}".format(url)
        result_key = "result:{}".format(url)

        if redis_client.exists(result_key):
            redis_client.incr(count_key)
            return redis_client.get(result_key).decode("utf-8")

        result = fn(*args, **kwargs)
        redis_client.set(count_key, 0)
        redis_client.setex(result_key, 10, result)
        return result
    return wrapper


@cache_result
def get_page(url: str) -> str:
    """
    fetch and returns the content of a url

    Args:
        url (str): url to get

    Return:
        content of the url
    """
    response = requests.get(url)
    return response.text
