from django.contrib import admin
from django.urls import path, include


from .views import *

urlpatterns = [
    path('', DiscussionViewSet.as_view({'get': 'get'})),
    path('<name>', DiscussionViewSet.as_view({'get': 'get_detail'})),
    path('disc/<name>', DiscussionViewSet.as_view({'get': 'get_discussion_by_course'})),
    path('lesson/<name>', DiscussionViewSet.as_view({'get': 'get_discussion_by_lesson'})),

]
