from django.urls import path
from .views import cart_view, checkout, update_cart_item, remove_from_cart, checkout_api_view

urlpatterns =[
    path('cart-add/', cart_view),
    path('update-cart-item/', update_cart_item),
    path('remove-from-cart/', remove_from_cart),
    path('checkout-api-view/', checkout_api_view),
]

