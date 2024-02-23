# ecommerce_app/views.py
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer


def index(request):
    return render(request, "index.html")


@api_view(["GET"])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["POST"])
def add_to_cart(request):
    # Assuming data in request is {'product_id': 1, 'quantity': 2}
    serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_cart_items(request):
    cart_items = CartItem.objects.all()
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def remove_from_cart(request, id):
    cart_item = get_object_or_404(CartItem, pk=id)
    cart_item.delete()
    return Response(status=204)
