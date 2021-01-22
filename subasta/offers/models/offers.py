"""Offer model."""


# Django
from django.db import models


# Utilities
from subasta.utils.models import SubastaModel


class Offer(SubastaModel):
    """Offer model.

    An offer is when the customer proposes his price for the product."""


    user        = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product     = models.ForeignKey('products.Product', on_delete=models.CASCADE) 
    price_offer = models.DecimalField('Product offer price', max_digits=10, decimal_places=2)

    
    def __str__(self):
        """Return product offer."""
        return f'{self.product.name}, Q {self.price_offer}'

        
