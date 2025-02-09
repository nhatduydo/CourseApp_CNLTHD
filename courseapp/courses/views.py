from courses import paginators, serializers
from courses.models import Category, Comment, Course, Lesson, User
from django.shortcuts import render
from rest_framework import generics, parsers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import perms

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySeializer

    def get_queryset(self):
        queries = self.queryset

        # q = self.request.GET.get("q")
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)
        return queries


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePpaginator

    def get_queryset(self):
        queries = self.queryset

        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries

    # nếu detail=True => có biến tham số pk ở hàm
    # nếu detail=False => không có biến tham số pk ở hàm
    # pk: tham số id: đại diện cho model Course
    @action(methods=["get"], detail=True)
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True).all()

        # # thử debug
        # import pdb
        # pdb.set_trace()

        return Response(
            serializers.LessonSerializer(
                lessons, many=True, context={"request": request}
            ).data,
            status=status.HTTP_200_OK,
        )


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = serializers.LessonSerializer
    permission_classes = [perms.AllowAny]  # ai cũng được
    # tùy nhiên, ở dưới thì phải xác thực mới được comment => thực hiện ghi đè

    def get_permissions(self):
        if self.action in ["add_comment"]:
            return [perms.IsAuthenticated()]
        return self.permission_classes

    @action(methods=["POST"], url_path="comments", detail=True)
    def add_comment(self, request, pk):
        # user đã chứng thực rồi sẽ nằm trong request.user
        # tất cả dữ liệu từ body data lấy từ client lấy lên đều trong: request.data
        c = Comment.objects.create(
            user=request.user,
            lesson=self.get_object(),
            content=request.data.get("content"),
        )

        return Response(
            serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED
        )


# để post và chèn vô => CreateAPIView
class UserViewset(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
    parser_classes = [
        parsers.MultiPartParser
    ]  # nhờ thằng này, nó sẽ tiến hành upload được tập tin của mình, upload hẳn lên cloudinary chứ không còn server

    def get_permissions(self):
        if self.action.__eq__("current_user"):
            return [perms.IsAuthenticated()]

        return [perms.AllowAny()]

    # nó gọi API này khi nó đã được chứng thực rồi
    @action(methods=["GET"], url_name="current-user", detail=False)
    def current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)


class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
