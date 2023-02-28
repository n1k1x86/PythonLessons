"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    data_len = len(data)
    if data_len < 3:
        return False
    a, b, c = 0, 1, 1
    while c != data[2]:
        a, b, c = b, c, b + c
    if [a, b, c] != data[:3]:
        return False
    a, b = data[0], data[1]
    for _ in range(data_len - 2):
        a, b = b, a + b
    if b == data[-1]:
        return True
    return False
