
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('userauth.urls')),
    path('api/user/', include('userprofile.urls')),
    path('api/courses/', include('course.urls')),
    path('api/quiz/', include('quiz.urls')),
    path('api/discussion/', include('discussion.urls')),
]
