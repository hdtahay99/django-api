"""User models admin."""


# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Models
from subasta.users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_admin', 'is_client')
    list_filter  = ('is_client', 'is_admin', 'created', 'modified')


admin.site.register(User, CustomUserAdmin) 