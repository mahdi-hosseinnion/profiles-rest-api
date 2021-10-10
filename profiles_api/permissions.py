from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own profile"""
        #safe method like (GET) does not matter
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
