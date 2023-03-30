"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if not nums:
        raise ValueError("You gave an empty array")
    if len(nums) < k:
        raise ValueError("Array's length is less than k")
    arr_length = len(nums)
    current_sum = 0
    greater_sum = 0
    for i in range(arr_length):
        k1 = 1
        while k1 <= k:
            current_sum = sum(nums[i:k1 + i])
            greater_sum = max(current_sum, greater_sum)
            k1 += 1
    return greater_sum
