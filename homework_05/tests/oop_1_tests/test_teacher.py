import pytest
from tasks.oop_1_classes.teacher import Teacher, WrongSecondNameError, WrongFirstNameError, WrongTaskDeadlineError, \
    WrongTaskTextError


@pytest.mark.parametrize('inp_data, expected_exception', [([None, "John"], WrongFirstNameError),
                                                          ([1234, "John"], WrongFirstNameError),
                                                          ([None, "John"], WrongFirstNameError),
                                                          (['Josh', None], WrongSecondNameError),
                                                          (['Nik', 1234], WrongSecondNameError),
                                                          (['None', None], WrongSecondNameError)])
def test_init_exceptions(inp_data, expected_exception):
    with pytest.raises(expected_exception):
        Teacher(*inp_data)


@pytest.mark.parametrize('task_text, task_deadline', [("Test task 1", 10),
                                                      ("Test task 2", 2),
                                                      ("Test task 3", 5)])
def test_create_homework_positive(task_text, task_deadline):
    test_teacher = Teacher('Test', 'Test')
    assert test_teacher.create_homework(task_text, task_deadline)


@pytest.mark.parametrize('inp_data, expected_exception', [([12, None], WrongTaskTextError),
                                                          ([None, 12], WrongTaskTextError),
                                                          (['Test task', None], WrongTaskDeadlineError),
                                                          (['Test task', '12'], WrongTaskDeadlineError)])
def test_create_homework_exceptions(inp_data, expected_exception):
    test_teacher = Teacher('Test', 'Test')
    with pytest.raises(expected_exception):
        test_teacher.create_homework(*inp_data)
