from django.http import JsonResponse
from rest_framework import viewsets
from .models import Post, Cats
from .serializers import PostSerializer, CatsSerializer
from django.shortcuts import render


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer


