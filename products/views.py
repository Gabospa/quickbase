""" Products Views. """

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ProductModelSerializer

# Models
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """ Client view set."""

    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    #permission_classes = [IsAuthenticated]