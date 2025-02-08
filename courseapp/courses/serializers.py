from courses.models import Category, Course, Lesson, Tag, User
from rest_framework import serializers


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source="image")
    tags = TagSerializer(many=True)

    def get_image(self, course):
        if course.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri("/static/%s" % course.image.name)


class CourseSerializer(BaseSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "subject", "image", "tags"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
        ]  # cái này trong model của django đã có sẵn những trường này rồi
