from django.contrib import admin
from .models import *

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id' ,'course_header', 'quiz_name']  
admin.site.register(Quiz, QuizAdmin)
