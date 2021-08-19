from django.shortcuts import render
from rest_framework import viewsets
from . models import Student
from . serializers import StudentSerializer

# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer