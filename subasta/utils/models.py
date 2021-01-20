"""Django models utilities."""

# Django
from django.db import models


class SubastaModel(models.Model):
    """Subasta base model"""

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now_add=True,
        help_text='Date time on which the object was modified'
    )

    class Meta:

        abstract      = True
        get_latest_by = 'created'
        ordering      = ['-created', '-modified']