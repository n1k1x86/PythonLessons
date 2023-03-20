"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

import string
from typing import Sequence, List


def custom_range(values: Sequence[str], start_elem: str, finish_elem: str = None, step: int = 1) -> List[str]:
    if finish_elem is None:
        return list(values[:values.index(start_elem):step])
    else:
        return list(values[values.index(start_elem):values.index(finish_elem):step])

