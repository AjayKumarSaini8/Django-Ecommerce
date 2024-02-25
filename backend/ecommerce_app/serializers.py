# ecommerce_app/serializers.py
from rest_framework import serializers
from .models import Product, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

    def validate(self, data):
        # Check if the product_id is valid (exists in Product model)
        product_id = data["product_id"]
        if not Product.objects.filter(pk=product_id).exists():
            raise serializers.ValidationError("Invalid product_id")

        # Add additional validation for quantity if needed
        # For example, ensure quantity is a positive integer

        return data
