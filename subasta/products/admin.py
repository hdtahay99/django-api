"""Products admin."""

# Django
from django.contrib import admin


# Model
from subasta.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin"""

    list_display = (
        'name',
        'price',
        'stock',
        'is_auctioned',
        'is_active'
    )

    search_fields = ('price', 'name', 'is_auctioned')
    list_filter = (
        'is_auctioned',
        'is_active',
    )