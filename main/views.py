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


@api_view(['GET'])
def cart_view(request):
    basket = 0
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
    else:
        basket = 0  # Set to 0 if user is not authenticated

    products = []
    total = 0

    if basket != 0:
        product_counts = Basket.objects.filter(user_id=user.id).values('product').annotate(count=Count('id'))
        duplicate_products = [(product_count['product'], product_count['count']) for product_count in product_counts]

        for product_id, count in duplicate_products:
            product = Product.objects.get(id=product_id)
            products.append({'name': product.name, 'number': count, 'common': count * product.price})
            total += count * product.price

    context = {
        'products': products,
        'basket': basket,
        'total': total,
    }

    ser = BasketSer(Basket.objects.filter(user_id=user.id), many=True)  # Serialize the basket queryset
    return Response(
        {'basket_data': ser.data, 'context': context})  # Return serialized data along with other context information
