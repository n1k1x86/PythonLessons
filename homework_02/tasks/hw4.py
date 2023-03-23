"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable
import time


def cache(func: Callable) -> Callable:
    func_cache = {}

    def make_cache(*args):
        if not func_cache.get(args):
            temp = func(*args)
            func_cache[args] = temp
        return func_cache[args]

    return make_cache
