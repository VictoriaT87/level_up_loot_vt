from django.shortcuts import render, reverse
from products.models import Product
from django.core.mail import send_mail
from django.contrib import messages
import random

from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    """
    View to return index page
    """
    products = Product.objects.all()

    featured_products = list(Product.objects.filter(is_featured=True))
    if len(featured_products) > 5:
        featured_products = random.sample(featured_products, 5)

    context = {
        "products": products,
        "featured_products": featured_products,
    }
    return render(request, "home/index.html", context)


def faqs(request):
    """
    FAQs Page
    """
    return render(request, "home/faqs.html")


def privacy_policy(request):
    """
    FAQs Page
    """
    return render(request, "home/privacy_policy.html")


def contact(request):
    """View to return Contact Us form"""
    if request.method == "POST":
        message_name = request.POST["name"]
        message_email = request.POST["email"]
        message = request.POST["message"]

        send_mail(
            "message from " + message_name,
            message + " reply to this message " + message_email,
            message_email,
            ["victoriaemt@gmail.com"],
        )
        messages.success(
            request, "Thank you, your email has been sent. We will contact you shortly."
        )
        return render(request, "home/contact.html")
    else:
        return render(request, "home/contact.html")
