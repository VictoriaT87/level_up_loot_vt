from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, f'{product.title} is already in your Wishlist!')
    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.title} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))


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