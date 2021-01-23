"""Sales admin."""

# Django
from django.contrib import admin


# Model
from subasta.sales.models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """Sale admin"""

    list_display = (
        'id',
        'offer',
        'total',
        'date_sale',
        'is_active'
    )

    search_fields = ('offer', 'date_sale')
    list_filter = (
        'date_sale',
    )