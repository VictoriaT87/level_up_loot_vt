from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path(
        "checkout_success/<order_number>",
        views.checkout_success,
        name="checkout_success",
    ),
    path("cache_checkout_data/", views.cache_checkout_data, name="cache_checkout_data"),
    path("wh/", webhook, name="webhook"),
    path("add_coupon/", views.add_coupon, name="add_coupon"),
    path("remove_coupon/", views.remove_coupon, name="remove_coupon"),
]
