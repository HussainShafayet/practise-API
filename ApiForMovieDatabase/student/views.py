from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from . models import Student
from . serializers import StudentSerializer

# Create your views here.
""" class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer """
@csrf_exempt
def studentView(request):
    """ if request.method == 'GET':
        student_info = Student.objects.all()
        serializer = StudentSerializer(student_info, many=True)
        return JsonResponse(serializer.data, safe=False)
    el """
    if request.method == 'POST':
        
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)