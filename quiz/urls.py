from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', QuizViewSet.as_view({'get': 'get'})),
    path('<name>', QuizViewSet.as_view({'get': 'get_detail'})),
    path('courses/<name>', QuizViewSet.as_view({'get': 'get_quiz_by_course'})),

]
