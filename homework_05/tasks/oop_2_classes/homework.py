import datetime


class Homework(object):
    def __init__(self, text: str, deadline_days: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline_days)
        self.created = datetime.datetime.now()

    def __str__(self):
        return self.text

    def is_active(self) -> bool:
        current_day = datetime.datetime.now()
        return (current_day - self.created).days < self.deadline.days


class NotHomeworkObject(Exception):
    pass


class HomeworkResult(object):
    def __init__(self, author, homework, solution: str):
        if not isinstance(homework, Homework):
            raise NotHomeworkObject("You gave a not Homework object")
        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = datetime.timedelta(days=datetime.datetime.now().day)
