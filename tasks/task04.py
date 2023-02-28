"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List

from collections import Counter


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Create a counter dictionary with sums A[i] + B[j]"""
    sum1 = Counter([i + j for i in a for j in b])
    """Create a counter dictionary with sums C[k] + D[l]"""
    sum2 = Counter([k + l for k in c for l in d])
    count = 0
    for key in sum1:
        count += sum1[key] * sum2[-key]
    return count
