from ckeditor.fields import RichTextField
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField('first_name', max_length=20, blank=False, null=False)
    last_name = models.CharField('last_name', max_length=30, blank=False, null=False)
    age = models.PositiveSmallIntegerField('age', blank=True, null=True)

    def __str__(self):
        return self.last_name


class Course(models.Model):
    name = models.CharField('name', max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField('first_name', max_length=20, blank=False, null=False)
    last_name = models.CharField('last_name', max_length=30, blank=False, null=False)
    age = models.PositiveSmallIntegerField('age', blank=True, null=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)
    is_study = models.BooleanField('is_study', default=True)
    about_me = RichTextField(blank=True, null=True)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # PROTECT, SET_NULL, SET_DEFAULT, DO_NOTHING
    course = models.ManyToManyField(Course, through='CourseStudent')

    def __str__(self):
        return self.last_name


class CourseStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField('date')