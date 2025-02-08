from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from courses.models import Category
from courses import serializers
from courses.models import Course
from courses import paginators


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySeializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePpaginator
