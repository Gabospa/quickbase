""" Client serializers."""

# Django REST Framework
from rest_framework import serializers

# Models 
from .models import Client


class ClientModelSerializer(serializers.ModelSerializer):
    """ Client model serializer. """

    class Meta:
        model = Client
        fields = '__all__'