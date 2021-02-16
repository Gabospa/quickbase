""" Bills admin."""

# Django
from django.contrib import admin

# Model
from .models import Bill

admin.site.register(Bill)