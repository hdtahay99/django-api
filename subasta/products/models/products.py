"""Product model."""

# Django
from django.db import models


# Utilities
from subasta.utils.models import SubastaModel


class Product(SubastaModel):
    """Product model.

    A product is an item that can be auctioned."""

    name         = models.CharField('product name', max_length=255)
    price        = models.DecimalField('product price', max_digits=10, decimal_places=2)
    stock        = models.PositiveIntegerField('product stock') 
    is_auctioned = models.BooleanField(
        'Auctioned product',
        default=False,
        help_text='Check if the products have already been auctioned'
    ) 
    is_active    = models.BooleanField(
        'Actived product',
        default=True,
        help_text='Check if the products are available'
    )


    def __str__(self):
        """Return product name."""
        return self.name

    
    class Meta(SubastaModel.Meta):
        """Meta class."""

        ordering = ['-name']

