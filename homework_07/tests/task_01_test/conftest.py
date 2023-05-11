import pytest
import os


@pytest.fixture(autouse=True)
def create_text_file():
    file_names = ['testfile01.txt', 'testfile02.txt', 'testfile03.txt']
    for file in file_names:
        with open(file, 'w'):
            pass
    yield
    for file in file_names:
        os.remove(file)
