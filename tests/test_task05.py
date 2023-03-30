from tasks import task05
import pytest


@pytest.mark.parametrize('nums, k, expected_res', [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
                                                   ([1, 3, -1, -3, 5, 3, 6, 7], 4, 21),
                                                   ([1, 3, -1, -3, 5, 3, 6, 7], 2, 13),
                                                   ([1, 3, -1, -3, 5, 3, 6, 7, 45, 32, 1, 4], 6, 98)])
def test_find_maximal_subarray_sum_positive(nums, k, expected_res):
    assert task05.find_maximal_subarray_sum(nums, k) == expected_res


@pytest.mark.parametrize('nums, k, not_expected_res', [([1, 3, -1, -3, 5, 3, 6, 7], 3, 13),
                                                       ([1, 3, -1, -3, 5, 3, 6, 7], 4, 29),
                                                       ([1, 3, -1, -3, 5, 3, 6, 7], 2, 11),
                                                       ([1, 3, -1, -3, 5, 3, 6, 7, 45, 32, 1, 4], 6, 4)])
def test_find_maximal_subarray_sum_negative(nums, k, not_expected_res):
    assert task05.find_maximal_subarray_sum(nums, k) != not_expected_res


@pytest.mark.parametrize('inp, k, expected_exception', [(123, 3, TypeError),
                                                        (None, 2, ValueError),
                                                        (13, 3, TypeError),
                                                        (1010101010, 10, TypeError),
                                                        (None, 10, ValueError)])
def test_find_maximal_subarray_sum_exceptions(inp, k, expected_exception):
    with pytest.raises(expected_exception):
        task05.find_maximal_subarray_sum(inp, k)
