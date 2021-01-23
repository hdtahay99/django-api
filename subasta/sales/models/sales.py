"""Sale model."""

# Django
from django.db import models


# Utilities
from subasta.utils.models import SubastaModel


class Sale(SubastaModel):
    """ Sale model.

    A sale contain the product offered."""

    offer     = models.ForeignKey('offers.Offer', on_delete=models.CASCADE) 
    total     = models.DecimalField('total sale', max_digits=10, decimal_places=2)
    date_sale = models.DateField('date sale')
    is_active = models.BooleanField(
        'Sale active',
        default=True,
        help_text='Check if the sale is active'
    )


    def __str__(self):
        """Return the sale."""
        return f"{self.offer}, {self.total}"
        

    class Meta(SubastaModel.Meta):
        """Meta class."""

        ordering = ['-date_sale']
