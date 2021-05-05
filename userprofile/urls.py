from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('profile/<name>', UserProfileViewSet.as_view({'get': 'get_profile'})),
    path('profile/insert/', UserProfileViewSet.as_view({'post': 'post_profile'})),
    path('profile/update/<name>',UserProfileViewSet.as_view({'put': 'put_profile'}))
]
