from django.urls import path
from .views import cart_view, checkout, update_cart_item, remove_from_cart

urlpatterns =[
    path('cart-add/', cart_view),
    path('check-out/', checkout),
    path('update-cart-item/', update_cart_item),
    path('remove-from-cart/', remove_from_cart),
]

