from courses.models import Category
from courses.models import Course
from rest_framework import serializers


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
