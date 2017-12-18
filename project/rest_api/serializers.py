from django.contrib.auth.models import User
from rest_framework import serializers
from project.rest_api.models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url','name','marks','subject')
