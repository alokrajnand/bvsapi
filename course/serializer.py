from rest_framework import serializers
from .models import *
from rest_framework import exceptions


# ******************************************************************
# course serializer
# *******************************************************************

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseRatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ratings
        fields = "__all__"
