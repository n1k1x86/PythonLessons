import pytest
import os


@pytest.fixture(autouse=True)
def create_text_file():
    with open("test_text_file.txt", 'w'):
        pass
    yield
    os.remove("test_text_file.txt")
