from django.contrib import admin
from .models import Product, CartItem


class ProductAdmin(admin.ModelAdmin):
    # Define how the admin should display the model's fields
    list_display = ("id", "name", "price", "description", "image_url")
    search_fields = ("name",)  # Add fields for searching


class CartAdmin(admin.ModelAdmin):
    # Define how the admin should display the model's fields
    list_display = ("id", "product_id", "quantity")
    search_fields = "id"  # Add fields for searching


# Register your models with the admin site
admin.site.register(Product, ProductAdmin)
