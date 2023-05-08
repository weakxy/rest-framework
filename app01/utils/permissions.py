from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        user_type = request.user.permissions
        if user_type == 3:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        pass
