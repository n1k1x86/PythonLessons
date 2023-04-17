from collections import defaultdict

from tasks.oop_2_classes.homework import Homework, HomeworkResult
from tasks.oop_2_classes.person import Person


class Teacher(Person):
    homework_done = defaultdict()

    def __init__(self, first_name: str, last_name: str = None):
        super().__init__(first_name, last_name)

    @staticmethod
    def create_homework(task_text: str, task_deadline: str):
        return Homework(task_text, task_deadline)

    @classmethod
    def check_homework(cls, home_res: HomeworkResult):
        if len(home_res.solution) > 5:
            cls.homework_done[home_res.homework] = home_res
            return True
        return False

    @classmethod
    def reset_results(cls, hw: Homework = None):
        if hw:
            del cls.homework_done[hw]
        cls.homework_done.clear()

