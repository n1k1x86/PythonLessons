from tasks.task_02 import backspace_compare
import pytest


@pytest.mark.parametrize('first, second', [('a#b#c', 'b##c'),
                                           ('a#b#c###', ''),
                                           ('a#bc', 'b##bcb#'),
                                           ('a##a#ab', 'ab')])
def test_backspace_positive(first, second):
    assert backspace_compare(first, second)


@pytest.mark.parametrize('first, second', [('a#b#c', 'b##ca'),
                                           ('a#b#c###', 'abc'),
                                           ('a#bc', 'b##bb#'),
                                           ('a#aa#ab', 'a')])
def test_backspace_negative(first, second):
    assert not backspace_compare(first, second)


@pytest.mark.parametrize('first, second, expected_exception', [(None, 'a', TypeError),
                                                               (None, None, TypeError),
                                                               ('r', None, TypeError)])
def test_backspace_exceptions(first, second, expected_exception):
    with pytest.raises(expected_exception):
        backspace_compare(first, second)
