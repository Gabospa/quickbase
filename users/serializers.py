""" Users serializers."""

# Django
from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from .models import User

# Utilities
from datetime import timedelta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer. """

    class Meta:
        model = User
        fields = ('email', 'username')


class UserSignUpSerializer(serializers.Serializer):
    """ Serializer for User creation."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=6, max_length=20)
    password_confirmation = serializers.CharField(min_length=6, max_length=20)

    def validate(self, data):
        """ Validate correct passwords """
        pass_temp = data['password']
        pass_temp_confirmation = data['password_confirmation']
        if pass_temp != pass_temp_confirmation:
            raise serializers.ValidationError("Passwords are not equal")

        password_validation.validate_password(pass_temp)
        return data 

    def create(self, data):
        """ Create new user """
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user
    

