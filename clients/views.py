""" Clients Views. """

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ClientModelSerializer

# Models
from .models import Client

# Utils
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class ClientViewSet(viewsets.ModelViewSet):
    """ Client view set."""

    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def read_csv(request):
    """ Function to add Clients from CSV."""
    file =  BASE_DIR / 'MOCK_DATA.csv'

    with open(file, mode='r') as f:
        clients = csv.DictReader(f)
        for row in clients:
            client = Client(**row)
            client.save()
            print(client.first_name)
    return Response(status=status.HTTP_201_CREATED)