from courses.admin import admin_site
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Course API",
        default_version="v1",
        description="APIs for CourseApp",
        contact=openapi.Contact(email="nhatduy242@gmail.com"),
        license=openapi.License(name="DoNhatDuy"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", include("courses.urls")),
    path("admin/", admin_site.urls),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    re_path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("__debug__", include("debug_toolbar.urls")),
    # path("", views.home, name="home"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
