from rest_framework.pagination import PageNumberPagination


class CoursePpaginator(PageNumberPagination):
    page_size = 2
