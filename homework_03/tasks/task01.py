from typing import Callable


def cache(count: int) -> Callable:
    """Parameterizable function that caches functions' result n-times"""
    cache_dict = {'count': count, 'saved_value': None}

    def cache_sub(func: Callable) -> Callable:
        def wrapper(*args):
            if cache_dict.get('saved_value') and cache_dict['count'] > 0:
                cache_dict['count'] -= 1
                return cache_dict['saved_value']
            else:
                cache_dict['saved_value'] = func(*args)
                return cache_dict['saved_value']

        return wrapper

    return cache_sub


