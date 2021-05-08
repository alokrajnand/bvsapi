from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]

admin.site.register(Profile, UserProfileAdmin)
