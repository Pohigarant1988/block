from django.http import JsonResponse
from rest_framework import viewsets
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from django.shortcuts import render


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


