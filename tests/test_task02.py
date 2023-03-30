from tasks import task02
import pytest

from typing import List


@pytest.mark.parametrize('sequence', [([0, 1, 1, 2, 3, 5, 8]),
                                      ([2, 3, 5, 8]),
                                      ([8, 13, 21, 34, 55]),
                                      ([55, 89, 144, 233]),
                                      ([0, 1, 1])])
def test_check_fib_positive(sequence: List):
    assert task02.check_fibonacci(sequence)


@pytest.mark.parametrize('sequence', [([0, 1, 2, 3, 5, 8]),
                                      ([0, 2, 2, 5, 9])])
def test_check_fib_negative(sequence: List):
    assert not task02.check_fibonacci(sequence)


@pytest.mark.parametrize('sequence, exception', [(12345, TypeError),
                                                 (345, TypeError),
                                                 (123124, TypeError)])
def test_check_fib_exceptions(sequence: List, exception: Exception):
    with pytest.raises(exception):
        task02.check_fibonacci(sequence)
