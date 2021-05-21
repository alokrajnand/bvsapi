from django.db import models
from datetime import datetime
from course.models import *

# **********************************************************
# Quiz  Model
# *********************************************************


class Quiz(models.Model):
    course_header = models.ForeignKey(Course, to_field='course_header', on_delete=models.CASCADE)
    quiz_header = models.CharField(max_length=50, unique=True, null=False, default="")
    quiz_name = models.CharField(max_length=50, unique=True, null=False)
    quiz_desc = models.CharField(max_length=50,  null=False)
    quiz_no_of_question = models.CharField(max_length=50, null=True)
    quiz_difculty_level = models.CharField(max_length=100, null=True)
    quiz_rating = models.CharField(max_length=5000, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class Question(models.Model):
    quiz_header = models.CharField(max_length=50,  null=False, default="")
    course_header = models.CharField(max_length=50, unique=True, null=False, default="")
    question = models.CharField(max_length=150,  null=True)
    option_one = models.CharField(max_length=100, null=True)
    option_two = models.CharField(max_length=100, null=True)
    option_three = models.CharField(max_length=100, null=True)
    option_four = models.CharField(max_length=100, null=True)
    correct_option = models.CharField(max_length=100, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__