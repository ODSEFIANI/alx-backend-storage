#!/usr/bin/env python3
"""
redis Exercise
"""
import redis
from typing import Callable, Union, Optional, Any
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''count
    '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    ''' cache class
    '''
    def __init__(self):
        ''' int
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()
    @count_calls
    def store(self, data: Union[str, float, bytes, int]) -> str:
        ''' storage
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Retrieve data from the cache, apply optional function,
        and return the value"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
    
    def get_int(self, key: str) -> int:
        """Retrieve data from the cache and convert it to an integer"""
        return self.get(key, fn=int)

    def get_str(self, key: str) -> str:
        """Retrieve binary data from the cache and decode it to a string using UTF-8"""
        binary_data = self.get(key)
        if binary_data is not None:
            return binary_data.decode('utf-8')
        else:
            return ""





def call_history(method: Callable) -> Callable:
    '''history
    '''
    input_key = "{}:inputs".format(method.__qualname__)
    output_key = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''function
        '''
        input_str = str(args)
        self._redis.rpush(input_key, input_str)

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, result)

        return result

    return wrapper


def replay(method: Callable):
    '''finction
    '''

    input_key = "{}:inputs".format(method.__qualname__)
    output_key = "{}:outputs".format(method.__qualname__)

    inputs = [eval(input_str.decode("utf-8")) for input_str in self._redis.lrange(input_key, 0, -1)]
    outputs = [output_str.decode("utf-8") for output_str in self._redis.lrange(output_key, 0, -1)]

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        print(f"{method.__qualname__}{input_args} -> {output}")

