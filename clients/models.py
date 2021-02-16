""" Models Clients """

# Django
from django.db import models


class Client(models.Model):
    """ Client model."""

    document = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=12 )
    last_name = models.CharField(max_length=12)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email