import pytest
from tasks.oop_1_classes.student import Student, WrongSecondNameError, WrongFirstNameError
from tasks.oop_1_classes.homework import Homework


@pytest.mark.parametrize('inp_data, expected_exception', [([None, "John"], WrongFirstNameError),
                                                          ([1234, "John"], WrongFirstNameError),
                                                          ([None, "John"], WrongFirstNameError),
                                                          (['Josh', None], WrongSecondNameError),
                                                          (['Nik', 1234], WrongSecondNameError),
                                                          (['None', None], WrongSecondNameError)])
def test_init_exceptions(inp_data, expected_exception):
    with pytest.raises(expected_exception):
        Student(*inp_data)


@pytest.mark.parametrize('homework', [Homework("The first test task", 10),
                                      Homework("The second test task", 1),
                                      Homework("The third test task", 4),
                                      Homework("The fourth test task", 2)])
def test_do_homework_positive(homework):
    test_student = Student('Test', 'Test')
    assert test_student.do_homework(homework)


@pytest.mark.parametrize('homework', [Homework("The first test task", 0),
                                      Homework("The second test task", 0),
                                      Homework("The third test task", 0),
                                      Homework("The fourth test task", 0)])
def test_do_homework_negative(homework):
    test_student = Student('Test', 'Test')
    assert not test_student.do_homework(homework)


@pytest.mark.parametrize('inp_data, expected_exception', [('', AttributeError),
                                                          (123, AttributeError),
                                                          ('Homework', AttributeError)])
def test_do_homework_exceptions(inp_data, expected_exception):
    test_student = Student('Test', 'Test')
    with pytest.raises(expected_exception):
        test_student.do_homework(inp_data)
