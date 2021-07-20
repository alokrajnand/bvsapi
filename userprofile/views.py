
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
# importing "random" for random operations
import random
from django.db import Error
from functions.generateOtp import *
from functions.sendEmail import *


# ******************************************************************
# user  profile viewset
# *******************************************************************

class UserProfileViewSet(viewsets.ViewSet):

    permission_classes = [AllowAny]

    def get_profile(self, request, name, *args, **kwargs):
        user_profile = Profile.objects.get(user_email_address=name)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    # insert data to profile when signup

    def post_profile(self, request, *args, **kwargs):
        
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  
            email_address = serializer.data.get('user_email_address')   
            print(email_address)
            otp = GenerateOtp(email_address)
            print(otp)
            ## call sen mail function to send otp 
            recipient = email_address
            subject="OTP From Binary Village"
            body= otp
            send_email(recipient, subject, body)
            ## 
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    
    
    # Update profile data
    def put_profile(self, request, name, pk=None):
        user_profile = Profile.objects.get(user_email_address=name)
        serializer = UserProfileSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
