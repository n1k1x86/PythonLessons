from tasks import hw4
import pytest
import time


def func_for_testing_cache(a, b):
    sum_nums = 1
    for i in range(a, b + 1):
        sum_nums *= i
    print(sum_nums)
    return sum_nums ** b


@pytest.mark.parametrize('a, b', [(2, 1000),
                                  (4, 700),
                                  (10, 540),
                                  (16, 340),
                                  (10, 230)])
def test_cache_positive(a, b):
    cache_func = hw4.cache(func_for_testing_cache)
    first_start_time = time.time()
    first_call = cache_func(a, b)
    first_end_time = time.time() - first_start_time

    second_start_time = time.time()
    second_call = cache_func(a, b)
    second_end_time = time.time() - second_start_time

    assert first_end_time > second_end_time


@pytest.mark.parametrize('a, b', [(2, 1000),
                                  (4, 700),
                                  (10, 540),
                                  (16, 340),
                                  (10, 230)])
def test_cache_negative(a, b):
    cache_func = hw4.cache(func_for_testing_cache)
    first_start_time = time.time()
    first_call = cache_func(a, b)
    first_end_time = time.time() - first_start_time

    second_start_time = time.time()
    second_call = cache_func(a, b)
    second_end_time = time.time() - second_start_time

    assert not (first_end_time > second_end_time) is False


@pytest.mark.parametrize('int_val, params, expected_exception', [(123, 1, TypeError),
                                                                 (234, 234, TypeError),
                                                                 (345345, 234234, TypeError),
                                                                 ('rersr', 234, TypeError),
                                                                 (None, 23, TypeError),
                                                                 ('32456', 76, TypeError),
                                                                 ('123', 13, TypeError)])
def test_cache_exceptions(int_val, params, expected_exception):
    val = hw4.cache(int_val)
    with pytest.raises(expected_exception):
        val(params)
