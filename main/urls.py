from django.urls import path
from .views import *

urlpatterns =[
    path('cart-add/', cart_view),
    path('update-cart-item/', update_cart_item),
    path('remove-from-cart/', remove_from_cart),
    path('checkout-api-view/', checkout_api_view),
    path('create-order-api-view/', create_order),
]

