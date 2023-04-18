from tasks.oop_1_classes.homework import Homework


class WrongFirstNameError(Exception):
    pass


class WrongSecondNameError(Exception):
    pass


class Student(object):
    def __init__(self, first_name: str, last_name: str = ''):
        if not isinstance(first_name, str):
            raise WrongFirstNameError
        if not isinstance(last_name, str):
            raise WrongSecondNameError
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework):
        if homework.is_active():
            return homework
        print("You're late!")
        return None
