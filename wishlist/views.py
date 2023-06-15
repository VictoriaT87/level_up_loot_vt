from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import Http404

from .models import Wishlist
from profiles.models import UserProfile
from products.models import Product

# Create your views here.


def view_wishlist(request):
    """
    Show a user's wishlist
    """

    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to add to your Wishlist."
        )
        return redirect(reverse("account_login"))

    user = get_object_or_404(UserProfile, user=request.user)
    # https://www.queworx.com/django/django-get_or_create/
    wishlist, created = Wishlist.objects.get_or_create(user=user.user)

    template_name = "wishlist/wishlist.html"
    context = {"wishlist": wishlist}
    return render(request, template_name, context)


def add_wishlist(request, product_id):
    """
    Add a view to show the wishlist
    """

    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to add to your Wishlist."
        )
        return redirect(reverse("account_login"))

    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlist = get_object_or_404(Wishlist, user=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, f"{product.title} is already on your Wishlist!")
    else:
        wishlist.products.add(product)
        messages.info(request, f"{product.title} has been added to your Wishlist!")

    return redirect(reverse("product_detail", args=[product_id]))


def remove_wishlist(request, product_id):
    """
    Remove an item from the wishlist
    """

    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to edit your Wishlist."
        )
        return redirect(reverse("account_login"))

    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get(user=request.user)

    wishlist.products.remove(product)
    messages.info(request, f"{product.title} has been removed from your Wishlist!")

    return redirect(reverse("wishlist"))
