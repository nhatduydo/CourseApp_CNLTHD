from courses import paginators, serializers
from courses.models import Category, Course, Lesson
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


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
