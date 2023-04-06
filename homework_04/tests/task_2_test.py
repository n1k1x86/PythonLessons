from tasks import task_2_mock_input
from pytest_mock import mocker
import requests


def fetch_text():
    return requests.get('https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen').text


def test_mock_input_positive(mocker):
    fake_resp = mocker.Mock()
    fake_resp.text = mocker.Mock(return_value=fetch_text())
    mocker.patch("tasks.task_2_mock_input", return_value=fake_resp)
    res = task_2_mock_input.count_dots_on_i(
        'https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen')
    assert res == 7657


def test_mock_input_negative(mocker):
    fake_resp = mocker.Mock()
    fake_resp.text = mocker.Mock(return_value=fetch_text())
    mocker.patch("tasks.task_2_mock_input", return_value=fake_resp)
    res = task_2_mock_input.count_dots_on_i(
        'https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen')
    assert res != 1000
