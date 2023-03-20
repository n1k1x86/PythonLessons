from tasks import hw5
import string
import pytest


@pytest.mark.parametrize('str_sequence, first_elem, last_elem, step, expected_result',
                         [(string.ascii_lowercase, 'g', None, 1, ['a', 'b', 'c', 'd', 'e', 'f']),
                          (string.ascii_lowercase, 'g', 'p', 1, ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']),
                          (string.ascii_lowercase, 'p', 'g', -2, ['p', 'n', 'l', 'j', 'h']),
                          ])
def test_custom_range_positive(str_sequence, first_elem, last_elem, step, expected_result):
    assert hw5.custom_range(str_sequence, first_elem, last_elem, step) == expected_result


@pytest.mark.parametrize('str_sequence, first_elem, last_elem, step, non_expected_result',
                         [(string.ascii_lowercase, 'g', None, 1, ['a', 'b', 'c', 'd', 'e', 'f', 'g']),
                          (string.ascii_lowercase, 'g', 'p', 1, ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']),
                          (string.ascii_lowercase, 'p', 'g', -2, ['p', 'n', 'l', 'j', 'h', 'g', 'f', 'e']),
                          ])
def test_custom_range_negative(str_sequence, first_elem, last_elem, step, non_expected_result):
    assert hw5.custom_range(str_sequence, first_elem, last_elem, step) != non_expected_result

