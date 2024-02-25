# from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from ecommerce_app.models import Product, CartItem
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from ecommerce_app.serializers import ProductSerializer, CartItemSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()

        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
