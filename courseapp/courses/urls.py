from courses import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

router.register("categories", views.CategoryViewSet, basename="categories")
router.register("courses", views.CourseViewSet, basename="courses")
router.register("lessons", views.LessonViewSet, basename="lessons")
router.register("users", views.UserViewset, basename="users")
router.register("comments", views.CommentViewSet, basename="comments")


urlpatterns = [
    path("", include(router.urls)),
]
