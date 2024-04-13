from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .serializers import BasketSer  # Import your Basket serializer
from .models import Basket, Product, Info  # Import your models


@api_view(['GET', 'POST'])
def cart_view(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            cart_items = Basket.objects.filter(user=user)
            serializer = BasketSer(cart_items, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "User is not authenticated"}, status=403)

    elif request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            product_id = request.data.get('product')
            quantity = request.data.get('quantity', 1)  # Default to 1 if quantity is not provided

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"message": "Product does not exist"}, status=404)

            cart_item, created = Basket.objects.get_or_create(user=user, product=product)
            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()

            serializer = BasketSer(cart_item)
            return Response(serializer.data, status=201)
        else:
            return Response({"message": "User is not authenticated"}, status=403)
