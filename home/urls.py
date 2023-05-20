from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("faqs", views.faqs, name="faqs"),
    path("contact", views.contact, name="contact"),
]
