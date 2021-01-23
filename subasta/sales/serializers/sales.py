"""Sales serializers"""


# Django REST Framework
from rest_framework import serializers


# Model
from subasta.sales.models import Sale


class SaleModelSerializer(serializers.ModelSerializer):
    """Sale model serializer."""


    class Meta:
        """Meta class."""

        model  = Sale
        fields = (
            'id', 'offer', 'total', 'date_sale', 'is_active'
        ) 

