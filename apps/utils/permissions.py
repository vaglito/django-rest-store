# Permissions for the app
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit or delete objects.
    All users can view (read-only access).
    """
    def has_permission(self, request, view):
        # Allow read-only access to all users
        if request.method in SAFE_METHODS:
            return True
        # Allow write access only to admin users
        return request.user and request.user.is_staff


class IsOwnerOrAdminOrReadOnly(BasePermission):
    """
    Allow owners to edit their own objects, admins can do anything, others can only read.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only methods for anyone
        if request.method in SAFE_METHODS:
            return True
        
        # Allow admin users full access
        if request.user and request.user.is_staff:
            return True

        # Allow object owners to edit (but not delete)
        return obj.user == request.user and request.method in ['PUT', 'PATCH']