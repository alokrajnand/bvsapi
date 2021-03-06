
# this is for login and logout authentication
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

class QuizViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        data = Quiz.objects.all()
        serializer =QuizSerializer(data, many=True)
        return Response(serializer.data)

    def get_detail(self, request, name):
        data = Quiz.objects.get(course_header_id=name)
        serializer = QuizSerializer(data)
        return Response(serializer.data)

    def get_quiz_by_course(self, request, name):
        data = Quiz.objects.filter(course_header_id=name)
        if (data.count() == 0):
            return Response([{
                'message': 'No Data',
                'status': 400
            }])
        else:
            serializer = QuizSerializer(data, many=True)
            return Response(serializer.data)



