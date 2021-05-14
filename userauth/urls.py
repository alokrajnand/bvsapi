from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('register/', UserViewSet),
    path('login/', LoginViewSet.as_view()),
    path('emailverify/',VarificationViewSet.as_view({'post': 'post_auth'})),
]
