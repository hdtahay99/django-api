"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


# Utilities
from subasta.utils.models import SubastaModel


class User(SubastaModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User."""

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique' : 'A user with that email already exists.'
        }
    )


    is_admin = models.BooleanField(
        'admin',
        default=False,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Admins are the main type of user.'
        )
    )

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the that buys the products'
        )
    )

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'is_admin']


    def __str__(self):
        """Return username"""
        return self.username

    
    def get_short_name(self):
        """Return username"""
        return self.username
