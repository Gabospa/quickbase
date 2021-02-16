""" Bill Views. """

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import BillModelSerializer, BillProductsSerializer

# Models
from .models import Bill, BillProducts


class BillViewSet(viewsets.ModelViewSet):
    """ Bill view set."""

    queryset = Bill.objects.all()
    serializer_class = BillModelSerializer
    #permission_classes = [IsAuthenticated]

class BillProductsViewSet(viewsets.ModelViewSet):
    """ Bill - products view set. """
    queryset = BillProducts.objects.all()
    serializer_class = BillProductsSerializer
    #permission_classes = [IsAuthenticated]
