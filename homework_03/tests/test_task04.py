from tasks import task04
import pytest


@pytest.mark.parametrize('num, expected', [(153, True),
                                           (370, True),
                                           (371, True),
                                           (407, True)])
def test_is_armstrong_positive(num: int, expected: bool):
    assert task04.is_armstrong(num) == expected


@pytest.mark.parametrize('num, expected', [(1534, False),
                                           (377, False),
                                           (31, False),
                                           (49, False)])
def test_is_armstrong_negative(num: int, expected: bool):
    assert task04.is_armstrong(num) == expected


@pytest.mark.parametrize('inp, expected', [(None, ValueError),
                                           (' ', ValueError),
                                           (3.41, ValueError),
                                           ])
def test_is_armstrong_exception(inp, expected: Exception):
    with pytest.raises(expected):
        task04.is_armstrong(inp)
