""" Bills serializers."""

# Django REST Framework
from rest_framework import serializers

# Models 
from .models import Bill, BillProducts
from products.models import Product

# Serializers
from products.serializers import ProductModelSerializer


class BillModelSerializer(serializers.ModelSerializer):
    """ Bill model serializer. """

    class Meta:
        model = Bill
        fields = ('company_name', 'nit', 'code', 'client_id')

class BillProductsSerializer(serializers.ModelSerializer):
    """ Bill - Products model serializer."""

    bill = serializers.CharField()
    products = serializers.CharField()

    class Meta:
        model = BillProducts
        fields = ['bill', 'products']

    def create(self, data):
        """ Create relation between Bill and products. """

        new_bill = Bill.objects.filter(pk=data['bill']).first()
        new_product = Product.objects.filter(pk=data['products']).first()

        new_bill_product = BillProducts.objects.create(
            products=new_product,
            bill=new_bill
        )
        return new_bill_product