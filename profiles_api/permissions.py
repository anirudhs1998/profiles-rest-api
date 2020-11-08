from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS: #GET is safe, Patch put are not safe
            return True

        return obj.id == request.user.id #The request to change user profile of ID is checked with the user's id to ensure he can
                                            # change only his profile
