"""Offers admin."""

# Django
from django.contrib import admin


# Model
from subasta.offers.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    """Offer admin"""

    list_display = (
        'id',
        'user',
        'product',
        'price_offer',
    )

    search_fields = ('product', 'price_offer')
    list_filter = (
        'price_offer',
    )