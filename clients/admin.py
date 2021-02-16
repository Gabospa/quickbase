""" Client admin."""

# Django
from django.contrib import admin

# Model
from .models import Client

admin.site.register(Client)