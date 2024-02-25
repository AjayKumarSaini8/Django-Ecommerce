# ecommerce_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product_list_create_view),
    path("products/", views.get_all_products, name="get_all_products"),
    path("products/<int:pk>", views.product_update_view),
    path("products/<int:pk>/", views.product_delete_view),
    path("products/<int:id>/", views.get_product_details, name="get_product_details"),
    path("cart/", views.get_cart_items, name="get_cart_items"),
    path("cart/<int:id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/", views.add_to_cart, name="add_to_cart"),
]
