from courses.models import Category
from courses.models import Course
from rest_framework import serializers
from courses.models import Tag


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source="image")
    tags = TagSerializer(many=True)

    def get_image(self, course):
        if course.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri("/static/%s" % course.image.name)

    class Meta:
        model = Course
        fields = "__all__"
