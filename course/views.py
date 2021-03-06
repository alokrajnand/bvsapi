
# this is for login and logout authentication
from django.http import response
from django.http.response import HttpResponseServerError
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login
from rest_framework.views import APIView
from django.shortcuts import render
# this is to send response to client
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # to resolve csrf issue
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
# model and serializer import
from .serializer import *
from .models import *
from django.core.mail import send_mail


# ******************************************************************
# Course
# *******************************************************************

class CourseViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        data = Course.objects.all()
        serializer = CourseSerializer(data, many=True)
        return Response(serializer.data)

    def get_detail(self, request, name):
        data = Course.objects.get(course_header=name)
        serializer = CourseSerializer(data)
        return Response(serializer.data)





# **********************************************************
# Lesson  ViewSet
# *********************************************************

class LessonViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_detail(self, request, name):
        data = Lesson.objects.filter(course_header=name)
        if (data.count() == 0):
            return Response([{
                'message': 'No Data',
                'status': 400
            }])
        else:
            serializer = LessonSerializer(data , many=True)
            return Response(serializer.data)


# ******************************************************************
# Ratings
# *******************************************************************

class RatingsViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get_ratings(self, request, name):
        data = Ratings.objects.filter(course_header=name)
        if (data.count() == 0):
            return response({
                'message': 'No Data',
                'status': 400
            })
        else:
            serializer = CourseRatingsSerializer(data, many=True)
            return Response(serializer.data)

