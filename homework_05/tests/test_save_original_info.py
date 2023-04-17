import pytest
from tasks.save_original_info import custom_sum


@pytest.mark.parametrize('first_elem, second_elem, expected_res', [(1, 2, 3),
                                                                   ([1, 2], [3, 4, 5, 6], [1, 2, 3, 4, 5, 6])])
def test_custom_sum(first_elem, second_elem, expected_res):
    assert custom_sum(first_elem, second_elem) == expected_res


def test_custom_sum_name():
    assert custom_sum.__name__ == 'custom_sum'


def test_custom_sum_orig_func():
    assert str(custom_sum.__original_func)[:20] == '<function custom_sum'


def test_custom_sum_doc():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
