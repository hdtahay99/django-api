"""Products serializers"""


# Django REST Framework
from rest_framework import serializers


# Model
from subasta.products.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    """Product model serializer."""


    class Meta:
        """Meta class."""

        model  = Product
        fields = (
            'id', 'name', 'price', 'stock', 'is_auctioned', 'is_active'
        ) 

