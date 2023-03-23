import pytest

from tasks import hw1


@pytest.mark.parametrize('file_name, expected_char', [('tests/hw1_test/get_rarest_char_test/test_data.txt', '›')])
def test_get_rarest_char(file_name, expected_char):
    assert hw1.get_rarest_char(file_name) == expected_char


@pytest.mark.parametrize('expected_exception, file_name',
                         [(FileNotFoundError, 'tests/hw1_test/get_rarest_char_test/not_exist_data.txt'),
                          (FileNotFoundError, 'tests/hw1_test/get_rarest_char_test/some_not_exist_data.txt'),
                          (FileNotFoundError, 'tests/hw1_test/get_rarest_char_test/not_found_data.txt'),
                          (OSError, 12345),
                          (OSError, 54321),
                          (OSError, 1234)])
def test_get_rarest_char_exceptions(expected_exception, file_name):
    with pytest.raises(expected_exception):
        hw1.get_rarest_char(file_name)
