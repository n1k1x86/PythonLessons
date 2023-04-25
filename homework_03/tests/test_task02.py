from typing import Callable

import mock

from time import time
from tasks import task02


def get_work_time(func: Callable):
    start = time()
    func()
    return time() - start


def test_slow_calc_positive():
    with mock.patch.object(task02, "__name__", "__main__"):
        assert task02.main() == 1024259


def test_slow_calc_negative():
    with mock.patch.object(task02, "__name__", "__main__"):
        assert not task02.main() != 1024259


def test_slow_calc_time():
    with mock.patch.object(task02, "__name__", "__main__"):
        assert get_work_time(task02.main) <= 60.0
