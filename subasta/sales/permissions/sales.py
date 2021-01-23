"""Products permissions classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission


# Models
from subasta.users.models import User

class IsUserAdmin(BasePermission):
    """Allow access only the admin users."""


    def has_permission(self, request, view):
        """Check that the user is admin."""

        if view.action in ['list', 'create',' upadte', 'partial_update']:
            return request.user.is_authenticated and request.user.is_admin
        else:
            return False

