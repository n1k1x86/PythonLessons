from tasks import hw1
import pytest


@pytest.mark.parametrize('file_name, expected_count',
                         [('tests/hw1_test/count_punctuation_chars_test/test_data.txt', 5305)])
def test_count_punctuation_chars_positive(file_name, expected_count):
    assert hw1.count_punctuation_chars(file_name) == expected_count


@pytest.mark.parametrize('file_name, wrong_count', [('tests/hw1_test/count_punctuation_chars_test/test_data.txt', 530),
                                                    ('tests/hw1_test/count_punctuation_chars_test/test_data.txt', 5301),
                                                    ('tests/hw1_test/count_punctuation_chars_test/test_data.txt', 4532),
                                                    ('tests/hw1_test/count_punctuation_chars_test/test_data.txt', 1234),
                                                    ('tests/hw1_test/count_punctuation_chars_test/test_data.txt', 6078),
                                                    (
                                                    'tests/hw1_test/count_punctuation_chars_test/test_data.txt', 3456)])
def test_count_punctuation_chars_negative(file_name, wrong_count):
    assert hw1.count_punctuation_chars(file_name) != wrong_count


@pytest.mark.parametrize('expected_exception, file_name',
                         [(FileNotFoundError, 'tests/hw1_test/count_punctuation_chars_test/some_test_data.txt'),
                          (FileNotFoundError, 'tests/hw1_test/count_punctuation_chars_test/not_exist_test_data.txt'),
                          (FileNotFoundError, 'tests/hw1_test/count_punctuation_chars_test/not_exist_database.txt'),
                          (OSError, 1345),
                          (OSError, 54321),
                          (OSError, 12389)])
def test_get_rarest_char_exceptions(expected_exception, file_name):
    with pytest.raises(expected_exception):
        hw1.count_punctuation_chars(file_name)
