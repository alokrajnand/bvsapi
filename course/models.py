from django.db import models
from datetime import datetime


# **********************************************************
# Course  Model
# *********************************************************


class Course(models.Model):
    course_header = models.CharField(max_length=50, unique=True, null=False)
    course_name = models.CharField(max_length=50, unique=True, null=False)
    course_category = models.CharField(max_length=50,  null=False)
    course_pic_url= models.CharField(max_length=100,  null=True)
    course_author = models.CharField(max_length=50, null=True)
    course_short_desc = models.CharField(max_length=100, null=True)
    course_desc = models.CharField(max_length=5000, null=True)
    lesson_count= models.IntegerField(default="10" , null= False)
    quiz_count= models.IntegerField(default="10" , null= False)
    total_enrolled=models.IntegerField(default="10" , null= False)
    course_like= models.IntegerField(default="100" , null= False)
    course_reviewed=models.IntegerField(default="100" , null= False)
    course_hour=models.IntegerField(default="100" , null= False)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.course_header


# **********************************************************
# Lesson  Model
# *********************************************************

class Lesson(models.Model):
    lesson_header = models.CharField(max_length=50, unique=True, null=False , default="")
    lesson_id=models.IntegerField(default=0 , null=False, unique=True)
    course_header = models.ForeignKey(Course, to_field='course_header', on_delete=models.CASCADE) 
    course_name = models.CharField(max_length=50, null=False)  
    lesson_name = models.CharField(max_length=50,null=False)
    lesson_description = models.CharField(max_length=100, null=True)
    lesson_video_link = models.CharField(max_length=50, null=True)
    lesson_video_minute = models.IntegerField(default="30")
    lesson_about = models.CharField(max_length=1000, null=True)
    discussion_count = models.IntegerField(default="30")
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


# **********************************************************
# Like  Model
# *********************************************************

class Ratings(models.Model):
    course_header = models.ForeignKey(Course, to_field='course_header', on_delete=models.CASCADE)
    rated_by = models.CharField(max_length=50, unique=True, null=False)
    rating = models.CharField(max_length=100, null=True)
    rating_comment = models.CharField(max_length=50, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
