""" Users admin."""

# Django
from django.contrib import admin

# Model
from .models import User

admin.site.register(User)
