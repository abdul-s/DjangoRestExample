from rest_framework import viewsets

from project.rest_api.models import Student
from project.rest_api.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Student to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
