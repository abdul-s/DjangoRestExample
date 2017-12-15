from django.contrib.auth.models import User
from project.api.models import Student
from rest_framework import viewsets
from project.api.serializers import UserSerializer
from project.api.serializers import StudentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Student to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
