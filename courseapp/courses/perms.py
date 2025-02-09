from rest_framework import permissions


class OwnerAuthenticated(permissions.IsAuthenticated):
    pass