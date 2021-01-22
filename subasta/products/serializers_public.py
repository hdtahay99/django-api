"""Products serializers."""

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# Models
from subasta.products.models import Product


class ProductSerializer(serializers.Serializer):
    """Product serializer."""
    
    id           = serializers.ReadOnlyField()
    name         = serializers.CharField()
    price        = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock        = serializers.IntegerField()
    is_auctioned = serializers.BooleanField()


# class CreateProductSerializer(serializers.Serializer):
#     """Create product serializer."""

#     name  = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     stock = serializers.IntegerField()


#     def create(self, data):
#         """Create product"""
#         return Product.objects.create(**data)