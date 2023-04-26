from tasks import task_3_get_print_output
import pytest


@pytest.mark.parametrize('input_value, expected', [('OK', 'OK'),
                                                   ('GOOD', 'GOOD'),
                                                   ('NICE', 'NICE'),
                                                   ('BEAUTIFUL', 'BEAUTIFUL')])
def test_my_precious_logger_stdout(input_value, expected, capfd):
    task_3_get_print_output.my_precious_logger(input_value)
    out, err = capfd.readouterr()
    assert out == expected


@pytest.mark.parametrize('input_value, expected', [('error: file_not_found', 'error: file_not_found'),
                                                   ('error: wrong_file_descriptor', 'error: wrong_file_descriptor'),
                                                   ('error: index_out_of_range', 'error: index_out_of_range'),
                                                   ('error: database_is_not_exist', 'error: database_is_not_exist')])
def test_my_precious_logger_stdout(input_value, expected, capfd):
    task_3_get_print_output.my_precious_logger(input_value)
    out, err = capfd.readouterr()
    assert err == expected
