from tasks import task03
import pytest


@pytest.mark.parametrize('filename, expected_res', [('tests/test_task03/test_nums01.txt', (1, 789)),
                                                    ('tests/test_task03/test_nums02.txt', (-3, 234324234)),
                                                    ('tests/test_task03/test_nums03.txt', (-100, 34))])
def test_find_max_and_min_positive(filename: str, expected_res: tuple[int, int]):
    assert task03.find_maximum_and_minimum(filename) == expected_res


@pytest.mark.parametrize('filename, not_expected_res', [('tests/test_task03/test_nums01.txt', (1, 79)),
                                                    ('tests/test_task03/test_nums02.txt', (-3, 4234)),
                                                    ('tests/test_task03/test_nums03.txt', (-1, 34))])
def test_find_max_and_min_negative(filename: str, not_expected_res: tuple[int, int]):
    assert task03.find_maximum_and_minimum(filename) != not_expected_res


@pytest.mark.parametrize('inp, expected_exception', [('tests/test_task03/test_num1.txt', FileNotFoundError),
                                                     ('tests/test_task03/test_num2.txt', FileNotFoundError),
                                                     ('tests/test_task03/test_num3.txt', FileNotFoundError),
                                                     ('tests/test_task03/test_num4.txt', FileNotFoundError),
                                                     (1234, OSError),
                                                     (123432, OSError),
                                                     (123131234, OSError)])
def test_find_max_and_min_exceptions(inp, expected_exception: Exception):
    with pytest.raises(expected_exception):
        task03.find_maximum_and_minimum(inp)
