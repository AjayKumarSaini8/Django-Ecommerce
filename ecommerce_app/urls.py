# ecommerce_app/urls.py
from django.urls import path
from .views import (
    get_all_products,
    get_product_details,
    add_to_cart,
    get_cart_items,
    remove_from_cart,
)

urlpatterns = [
    path("products/", get_all_products, name="get_all_products"),
    path("products/<int:id>/", get_product_details, name="get_product_details"),
    path("cart/", get_cart_items, name="get_cart_items"),
    path("cart/<int:id>/", remove_from_cart, name="remove_from_cart"),
    path("cart/", add_to_cart, name="add_to_cart"),
]
