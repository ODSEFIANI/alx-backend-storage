#!/usr/bin/env python3
"""
redis Exercise
"""
import redis
from typing import Callable
import uuid
from functools import wraps


class Cache:
    ''' cache class
    '''
    def __init__(self):
        ''' int
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        ''' storage
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fct: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Retrieve data from the cache, apply optional function,
        and return the value"""
        value = self._redis.get(key)
        if fct:
            value = fct(value)
        return value
    
    def get_int(self, key: str) -> int:
        """Retrieve data from the cache and convert it to an integer"""
        return self.get(key, fct=int)

    def get_str(self, key: str) -> str:
        """Retrieve data from the cache and convert it to a string"""
        return self.get(key, fct=str)


def count_calls(method: Callable) -> Callable:
    '''count
    '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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


if __name__ == "__main__":
    pass  # You can add test cases or run the main program here
