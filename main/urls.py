from django.urls import path
from .views import cart_view

urlpatterns =[
    path('cart_add/', cart_view  )

]

