from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from .models import Wishlist
from profiles.models import UserProfile
from products.models import Product

# Create your views here.


@login_required
def view_wishlist(request):
    """
    Show a user's wishlist
    """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = get_object_or_404(Wishlist, user=user.user)

    template_name = 'wishlist/wishlist.html'
    context = {'wishlist': wishlist}
    return render(request, template_name, context)


@login_required
def add_wishlist(request, product_id):
    """
    Add a view to show the wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlist = get_object_or_404(Wishlist, user=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, 'The product is already in your wishlist!')
    else:
        wishlist.products.add(product)
        messages.info(request, 'Added the product to your wishlist')

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_wishlist(request, product_id):
    """
    Remove an item from the wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.get(user=request.user)

    wishlist.products.remove(product)
    messages.info(request, f'{product.title} has been removed from your Wishlist!')

    return redirect(reverse('wishlist'))