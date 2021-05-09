from django.contrib import admin
from .models import *

class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['id' ,'course_header', 'discussion_name']  
admin.site.register(Discussion, DiscussionAdmin)

