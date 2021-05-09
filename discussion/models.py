from django.db import models
from datetime import datetime
from course.models import *

# **********************************************************
# Quiz  Model
# *********************************************************


class Discussion(models.Model):
    course_header = models.ForeignKey(Course, to_field='course_header', on_delete=models.CASCADE)
    discussion_name = models.CharField(max_length=50, unique=True, null=False)
    discussion_desc = models.CharField(max_length=50,  null=False)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
