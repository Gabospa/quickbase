""" Product serializers."""

# Django REST Framework
from rest_framework import serializers

# Models 
from .models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    """ Products model serializer. """

    class Meta:
        model = Product
        fields = '__all__'