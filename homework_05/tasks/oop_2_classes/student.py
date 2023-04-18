from tasks.oop_2_classes.homework import Homework, HomeworkResult
from tasks.oop_2_classes.person import Person


class DeadlineError(Exception):
    pass


class Student(Person):
    def __init__(self, first_name: str, last_name: str = None):
        super().__init__(first_name, last_name)

    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            return HomeworkResult(self.first_name, homework, solution)
        else:
            raise DeadlineError("You're late!")
        return None
