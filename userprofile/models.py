from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
# write the code of user manager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime


# **********************************************************
# Profile Model
# *********************************************************

class Profile(models.Model):
    user_email_address = models.OneToOneField('userauth.User', to_field='email_address', primary_key=True , on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200, null=False)
    user_date_of_birth = models.DateField(null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number is not valid")
    user_phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=False, null=True),
    user_class=models.CharField(max_length=200, null=True)
    user_designation = models.CharField(max_length=200, null=True)
    user_tag_line = models.CharField(max_length=200, null=True)
    user_tag_line_desc = models.CharField(max_length=300, null=True)
    user_profile_pic_link = models.CharField(max_length=200, null=True)
    user_banner_pic_link = models.CharField(max_length=200, null=True)
    user_address = models.CharField(max_length=200, null=True)
    user_city = models.CharField(max_length=60, null=True)
    user_state = models.CharField(max_length=60, null=True)
    user_country = models.CharField(max_length=60, null=True)
    user_twitter_link = models.CharField(max_length=200, null=True)
    user_git_hub_link = models.CharField(max_length=200, null=True)
    user_linkdin_link = models.CharField(max_length=200, null=True)
    user_faebook_link = models.CharField(max_length=200, null=True)
    user_instagram_link = models.CharField(max_length=200, null=True)
    user_created_dt = models.DateTimeField(default=datetime.now, null=True)
    user_updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
