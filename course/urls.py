from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'get'})),
    path('<name>', CourseViewSet.as_view({'get': 'get_detail'})),
    path('lesson/<name>', LessonViewSet.as_view({'get': 'get_detail'})),
    path('ratings/<name>', RatingsViewSet.as_view({'get': 'get_ratings'})),

]
