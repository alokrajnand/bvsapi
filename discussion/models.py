from django.db import models
from datetime import datetime
from course.models import *

# **********************************************************
# Quiz  Model
# *********************************************************


class Discussion(models.Model):
    discussion_header = models.CharField(max_length=50, unique=True, null=False , default="")
    course_header = models.ForeignKey(Course, to_field='course_header', on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50, null=False)  
    lesson_header = models.ForeignKey(Lesson, to_field='lesson_header', on_delete=models.CASCADE)   
    lesson_name = models.CharField(max_length=50,null=False)
    discussion_name = models.CharField(max_length=50, unique=True, null=False, default="")
    discussion_desc = models.CharField(max_length=50,  null=False)
    discussion_views=models.IntegerField(null=True)
    discussion_ans_count=models.IntegerField(null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
