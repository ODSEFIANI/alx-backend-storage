#!/usr/bin/env python3
"""
redis Exercise
"""
import requests
import time
from typing import Callable

CACHE_EXPIRATION_SECONDS = 10
CACHE = {}

def cache_with_count(func: Callable) -> Callable:
    """
    Decorator that caches the result of a function with an expiration time
    and tracks the number of times the function is called.

    Args:
    - func (Callable): The function to be decorated.

    Returns:
    - Callable: Decorated function.
    """
    @wraps(func)
    def wrapper(url: str, *args, **kwargs) -> str:
        """
        Wrapper function that adds caching and counting functionality.

        Args:
        - url (str): The URL to access.
        - *args: Variable positional arguments.
        - **kwargs: Variable keyword arguments.

        Returns:
        - str: The content of the URL.
        """
        cache_key = f"count:{url}"
        if cache_key in CACHE and CACHE[cache_key]['expiration'] > time.time():
            CACHE[cache_key]['count'] += 1
            return CACHE[url]['content']

        result = func(url, *args, **kwargs)

        CACHE[cache_key] = {'count': 1, 'expiration': time.time() + CACHE_EXPIRATION_SECONDS}

        return result

    return wrapper

@cache_with_count
def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a URL using the requests module.

    Args:
    - url (str): The URL to access.

    Returns:
    - str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    fast_url = "http://www.google.com"

    # Access slow URL multiple times to observe caching and counting
    for _ in range(3):
        slow_content = get_page(slow_url)
        print(f"Slow URL content (cached): {slow_content}")
        time.sleep(2)

    # Access fast URL
    fast_content = get_page(fast_url)
    print(f"Fast URL content: {fast_content}")

    # Wait for cache expiration
    time.sleep(CACHE_EXPIRATION_SECONDS + 1)

    # Access slow URL after cache expiration
    slow_content_after_expire = get_page(slow_url)
    print(f"Slow URL content (after cache expiration): {slow_content_after_expire}")
