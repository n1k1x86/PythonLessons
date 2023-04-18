from tasks.oop_2_classes.homework import HomeworkResult, NotHomeworkObject
from tasks.oop_2_classes.teacher import Teacher
from tasks.oop_2_classes.student import Student

opp_teacher = Teacher('Daniil', 'Shadrin')
advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

lazy_student = Student('Roman', 'Petrov')
good_student = Student('Lev', 'Sokolov')

oop_hw = opp_teacher.create_homework('Learn OOP', 1)
docs_hw = opp_teacher.create_homework('Read docs', 5)

result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
result_3 = lazy_student.do_homework(docs_hw, 'done')


def test_class_name():
    assert opp_teacher.__class__.__name__ == 'Teacher'
    assert lazy_student.__class__.__name__ == 'Student'


def test_check_homework():
    assert opp_teacher.check_homework(result_1) is True
    assert opp_teacher.check_homework(result_3) is False


def test_homework_task():
    assert oop_hw.text == 'Learn OOP'


def test_homework_fail():
    try:
        HomeworkResult(good_student, "fff", "Solution")
    except NotHomeworkObject:
        return True
