"""Users serializers."""


# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.utils import timezone


# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


# Models
from subasta.users.models import User


# Utilities
import jwt
from datetime import timedelta


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta class"""

        model  = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'is_client'
        )


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data"""

    email    = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)


    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        self.context['user'] = user

        return data

    
    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.

    Handle sign up data validation and user client creation."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=15,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password              = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=2, max_length=64)
    
    first_name = serializers.CharField(min_length=2, max_length=64)
    last_name  = serializers.CharField(min_length=2, max_length=30) 

    def validate(self, data):
        """Verify passwords match."""

        passwd      = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")

        password_validation.validate_password(passwd)
        return data


    def create(self, data):
        """Handle user creation."""

        data.pop('password_confirmation')
        user    = User.objects.create_user(**data, is_admin=False)
        return user


    # def gen_verification_token(self, user):
    #     """Create JWT token that the user can use to verify its account."""

    #     exp_date = timezone.now() + timedelta(days=1)
    #     payload  = {
    #         'user' : user.username,
    #         'exp'  : int(exp_date.timestamp()),
    #         'type' : 'client'
    #     }
    #     token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    #     return token.decode()