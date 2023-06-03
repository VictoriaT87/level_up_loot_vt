from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("faqs", views.faqs, name="faqs"),
    path("privacy_policy", views.privacy_policy, name="privacy_policy"),
    path("contact", views.contact, name="contact"),
]
