"""Offers serializers."""


# Django REST Framework
from rest_framework import serializers


# Models
from subasta.offers.models import Offer


class OfferModelSerializer(serializers.ModelSerializer):
    """Offer model serializer"""

    class Meta:
        """Meta class"""

        model  = Offer
        fields = (
            'id',
            'user',
            'product',
            'price_offer',
        )


class CreateOfferSerializer(serializers.Serializer):
    """Create offer serializer."""

    user        = serializers.IntegerField()
    product     = serializers.IntegerField()
    price_offer = serializers.DecimalField(max_digits=10, decimal_places=2)


    def create(self, data):
        """Create product"""
        return Offer.objects.create(**data)