from tasks import hw1
import pytest


@pytest.mark.parametrize('file_name, expected_value',
                         [('tests/hw1_test/get_most_common_non_ascii_char_test/test_data.txt', 'ä')])
def test_count_non_ascii_chars_positive(file_name, expected_value):
    assert hw1.get_most_common_non_ascii_char(file_name) == expected_value


@pytest.mark.parametrize('file_name, wrong_count',
                         [('tests/hw1_test/get_most_common_non_ascii_char_test/test_data.txt', 530),
                          ('tests/hw1_test/get_most_common_non_ascii_char_test/test_data.txt', 5301),
                          ('tests/hw1_test/get_most_common_non_ascii_char_test/test_data.txt', 4532),
                          ('tests/hw1_test/get_most_common_non_ascii_char_test/test_data.txt', 1234),
                          ('tests/hw1_test/get_most_common_non_ascii_char_test/test_data.txt', 6078),
                          (
                                  'tests/hw1_test/get_most_common_non_ascii_char_test/test_data.txt', 3456)])
def test_count_punctuation_chars_negative(file_name, wrong_count):
    assert hw1.get_most_common_non_ascii_char(file_name) != wrong_count


@pytest.mark.parametrize('expected_exception, file_name',
                         [(FileNotFoundError, 'tests/hw1_test/get_most_common_non_ascii_char_test/some_test_data.txt'),
                          (FileNotFoundError,
                           'tests/hw1_test/get_most_common_non_ascii_char_test/not_exist_test_data.txt'),
                          (FileNotFoundError,
                           'tests/hw1_test/get_most_common_non_ascii_char_test/not_exist_database.txt'),
                          (OSError, 1345),
                          (OSError, 54321),
                          (OSError, 12389)])
def test_get_rarest_char_exceptions(expected_exception, file_name):
    with pytest.raises(expected_exception):
        hw1.get_most_common_non_ascii_char(file_name)
