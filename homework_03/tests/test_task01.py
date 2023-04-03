from tasks import task01
import pytest


def func_with_test(value: str, times: int) -> str:
    @task01.cache(times)
    def func_for_testing(inp="None"):
        return inp

    res = func_for_testing(value)
    for _ in range(times):
        res += func_for_testing()
    res += func_for_testing()
    return res


@pytest.mark.parametrize('value, times, expected', [('x', 3, 'xxxx'),
                                                    ('x', 4, 'xxxxx'),
                                                    ('x', 5, 'xxxxxx'),
                                                    ('x', 6, 'xxxxxxx'),
                                                    ('x', 7, 'xxxxxxxx')])
def test_cache_positive(value: str, times: int, expected: str):
    res = func_with_test(value, times)
    assert res[:-4] == expected


@pytest.mark.parametrize('value, times, not_expected', [('x', 4, 'xxxx'),
                                                        ('x', 5, 'xxxxx'),
                                                        ('x', 6, 'xxxxxx'),
                                                        ('x', 7, 'xxxxxxx'),
                                                        ('x', 8, 'xxxxxxxx')])
def test_cache_negative(value: str, times: int, not_expected: str):
    res = func_with_test(value, times)
    assert res[:-4] != not_expected


@pytest.mark.parametrize('value, times, expected_exception', [('x', '4', TypeError),
                                                              ('x', None, TypeError),
                                                              ('x', '6', TypeError),
                                                              ('x', None, TypeError),
                                                              ('x', '8', TypeError)])
def test_cache_exception(value: str, times, expected_exception: Exception):
    with pytest.raises(expected_exception):
        func_with_test(value, times)
