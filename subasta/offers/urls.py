"""Offer URls."""


# Django
from django.urls import path, include


# Views
from subasta.offers.views import create_offer


urlpatterns = [
    path('offers/product/', create_offer),
]
