from tasks import task_5_optional
import pytest


@pytest.mark.parametrize('num, expected', [(5, ["1", "2", "fizz", "4", "buzz"]),
                                           (4, ['1', '2', 'fizz', '4']),
                                           (10, ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz'])])
def test_fizzbuzz_positive(num, expected):
    assert list(task_5_optional.fizzbuzz(num)) == expected


@pytest.mark.parametrize('num, not_expected', [(3, ["1", "2", "buzz", "4", "fizz"]),
                                               (4, ['1', '2', 'buzz', '4']),
                                               (10,
                                                ['1', '2', 'buzz', '4', 'fizz', 'fizz', '7', '8', 'fizz', 'fizzbuzz'])])
def test_fizzbuzz_negative(num, not_expected):
    assert not list(task_5_optional.fizzbuzz(num)) == not_expected


@pytest.mark.parametrize('inp, expected_exception', [('3', TypeError),
                                                     ('65', TypeError),
                                                     (None, TypeError),
                                                     ('1234', TypeError)])
def test_fizzbuzz_exceptions(inp, expected_exception):
    with pytest.raises(expected_exception):
        list(task_5_optional.fizzbuzz(inp))
