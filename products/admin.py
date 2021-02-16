""" Product admin."""

# Django
from django.contrib import admin

# Model
from .models import Product

admin.site.register(Product)