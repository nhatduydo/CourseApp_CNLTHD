from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from courses.models import Category
from courses import serializers


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySeializer
