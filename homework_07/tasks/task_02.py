"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

#>>> with suppressor(IndexError):
...    [][2]
"""

from contextlib import contextmanager


@contextmanager
def suppressor_gen(exception):
    try:
        yield
    except exception:
        pass


class suppressor_class(object):
    def __init__(self, exception):
        self.exp = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, self.exp):
            return True
