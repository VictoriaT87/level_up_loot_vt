from django.urls import path
from . import views
from .views import DeleteProfile

urlpatterns = [
    path("", views.profile, name="profile"),
    path("order_history/<order_number>", views.order_history, name="order_history"),
    path("profile/user-delete/<int:pk>/", DeleteProfile.as_view(), name="user-delete"),
]
