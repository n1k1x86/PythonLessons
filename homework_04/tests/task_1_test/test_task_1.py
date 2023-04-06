from tasks import task_1_read_file
import pytest


def create_test_data(test_data):
    with open('test_text_file.txt', 'a') as f:
        f.writelines(test_data)


@pytest.mark.parametrize('test_data', ['1', '2', '1.432', '2.54'])
def test_read_file_positive(test_data):
    create_test_data(test_data)
    assert task_1_read_file.read_magic_number("test_text_file.txt")


@pytest.mark.parametrize('test_data', ['34', '20', '10.432', '20.54'])
def test_read_file_negative(test_data):
    create_test_data(test_data)
    assert not task_1_read_file.read_magic_number("test_text_file.txt")


@pytest.mark.parametrize('test_data, expected_exception', [(12, TypeError),
                                                           (34, TypeError),
                                                           (1, TypeError),
                                                           (None, TypeError)])
def test_read_file_exceptions(test_data, expected_exception):
    with pytest.raises(expected_exception):
        create_test_data(test_data)
