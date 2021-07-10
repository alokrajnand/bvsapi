from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id' ,'course_header', 'course_name','course_category']  

admin.site.register(Course, CourseAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_header_id', 'lesson_name']  

admin.site.register(Lesson, LessonAdmin)


class RatingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_header_id', 'rating','rated_by']  

admin.site.register(Ratings, RatingsAdmin)