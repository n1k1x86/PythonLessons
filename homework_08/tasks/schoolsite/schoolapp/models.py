from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=30)


class Homework(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=False)


class CompletedHomework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.PROTECT, blank=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, blank=False)
