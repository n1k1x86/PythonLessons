from tasks.oop_1_classes.homework import Homework


class WrongFirstNameError(Exception):
    pass


class WrongSecondNameError(Exception):
    pass


class WrongTaskTextError(Exception):
    pass


class WrongTaskDeadlineError(Exception):
    pass


class Teacher(object):
    def __init__(self, first_name: str, last_name: str = None):
        if not isinstance(first_name, str):
            raise WrongFirstNameError
        if not isinstance(last_name, str):
            raise WrongSecondNameError
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(task_text: str, task_deadline: int):
        if not isinstance(task_text, str):
            raise WrongTaskTextError
        if not isinstance(task_deadline, int):
            raise WrongTaskDeadlineError
        return Homework(task_text, task_deadline)
