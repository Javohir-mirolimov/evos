from django.urls import *
from . import views

urlpatterns = (
    path('user-register/', views.singup_view),
    path('user-login/', views.login_view),
    path('user-logout/', views.logout_view),
    path('user-update/<int:pk>/', views.edit_user_view),
    path('user-delete/<int:pk>/', views.delete_user),
)


