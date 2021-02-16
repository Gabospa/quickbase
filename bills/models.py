""" Bills Models """

# Django
from django.db import models

# Models
from clients.models import Client
from products.models import Product


class Bill(models.Model):
    """ Bill model."""

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.CharField(max_length=8)
    code = models.CharField(max_length=9, unique=True)
    products = models.ManyToManyField(Product, through='BillProducts')

    def __str__(self):
        return self.code


class BillProducts(models.Model):
    """ Bill products relation."""
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
