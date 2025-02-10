from courses.models import Category, Comment, Course, Lesson, Tag, User
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
        fields = ["id", "subject", "image", "tags", 'content', 'created_date', 'updated_date']


class LessonDetailSerializer(LessonSerializer):
    liked = serializers.SerializerMethodField()

    def get_liked(self, request, lesson):
        if request.user.is_authenticated:
            return lesson.like_set.filter(active=True).exists()

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['liked']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "avatar",
        ]  # cái này trong model của django đã có sẵn những trường này rồi
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data["password"])
        user.save()

        return user


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # để lấy avatar của user

    class Meta:  # thực hiện ghi đè
        model = Comment
        fields = ["id", "content", "user"]
