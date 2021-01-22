"""Offer URls."""


# Django
from django.urls import path, include


# Views
from subasta.offers.views import create_offer, list_offer_product, list_offers_product
# from .views import offers as offers_views



urlpatterns = [
    path('offers/product/', create_offer),
    path('offers/products/list/', list_offer_product),
    path('offers/product/list/', list_offers_product),

]
