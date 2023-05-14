from django.urls import path
from .import views

urlpatterns = [
    path('', views.view_wishlist, name='wishlist'),
    path('add_wishlist/<int:product_id>/', views.add_wishlist,
         name='add_wishlist'),
]