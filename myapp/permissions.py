from rest_framework import permissions

class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only authenticated users with the role "Instructor" can create, update, and delete courses
        return request.user.is_authenticated and request.user.role == 'Instructor'
