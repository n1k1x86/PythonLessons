import datetime


class WrongTextException(Exception):
    pass


class WrongDeadlineDaysException(Exception):
    pass


class Homework(object):
    def __init__(self, text: str, deadline_days: int):
        if not isinstance(text, str):
            raise WrongTextException
        if not isinstance(deadline_days, int):
            raise WrongDeadlineDaysException
        elif deadline_days < 0:
            raise WrongDeadlineDaysException
        self.text = text
        self.deadline = datetime.timedelta(days=deadline_days)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        current_day = datetime.datetime.now()
        return (current_day - self.created).days < self.deadline.days
