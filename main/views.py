from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BasketSer
from .models import Basket, Product, Info



@api_view(['GET', 'POST'])
def cart_view(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            cart_items = Basket.objects.filter(user=user)
            serializer = BasketSer(cart_items, many=True)
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            response_data = {
                "cart_items": serializer.data,
                "total_price": total_price
            }
            return Response(response_data)
        else:
            return Response({"message": "User is not authenticated"}, status=403)
    elif request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            product_id = request.data.get('product')
            quantity = request.data.get('quantity', 1)
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"message": "Product does not exist"}, status=404)
            cart_item, created = Basket.objects.get_or_create(user=user, product=product)
            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()
            serializer = BasketSer(cart_item)
            total_price = sum(item.product.price * item.quantity for item in Basket.objects.filter(user=user))
            response_data = {
                "cart_item": serializer.data,
                "total_price": total_price
            }
            return Response(response_data, status=201)
        else:
            return Response({"message": "User is not authenticated"}, status=403)

@api_view(['GET'])
def checkout_api_view(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(user_id=user.id).count()
        products = Basket.objects.filter(user_id=user.id)
    else:
        basket = 0
        products = []
    total = 0
    for i in products:
        total += i.product.price
    response_data = {
        'basket': basket,
        "total": total,
        'contact': Info.objects.last()
    }
    return Response(context)


@api_view(['PUT'])
def update_cart_item(request):
    user = request.user
    if not user.is_authenticated:
        return Response({"message": "User is not authenticated"}, status=status.HTTP_403_FORBIDDEN)
    cart_item_id = request.data.get('cart_item_id')
    new_quantity = request.data.get('quantity', 1)
    try:
        cart_item = Basket.objects.get(id=cart_item_id, user=user)
    except Basket.DoesNotExist:
        return Response({"message": "Cart item does not exist"}, status=status.HTTP_404_NOT_FOUND)
    cart_item.quantity = new_quantity
    cart_item.save()
    serializer = BasketSer(cart_item)
    total_price = sum(item.product.price * item.quantity for item in Basket.objects.filter(user=user))
    response_data = {
        "cart_item": serializer.data,
        "total_price": total_price
    }
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def remove_from_cart(request):
    user = request.user
    if not user.is_authenticated:
        return Response({"message": "User is not authenticated"}, status=status.HTTP_403_FORBIDDEN)
    cart_item_id = request.data.get('cart_item_id')
    try:
        cart_item = Basket.objects.get(id=cart_item_id, user=user)
        cart_item.delete()
        return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
    except Basket.DoesNotExist:
        return Response({"message": "Cart item does not exist"}, status=status.HTTP_404_NOT_FOUND)
