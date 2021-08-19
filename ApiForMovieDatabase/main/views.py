from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Movie, Comments
from .serializers import MovieSerializer,CommentSerializer

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class=CommentSerializer