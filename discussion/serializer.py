from quiz.models import Question
from rest_framework import serializers
from .models import *
from rest_framework import exceptions


# ******************************************************************
# course serializer
# *******************************************************************

class DiscussionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discussion
        fields = "__all__"


