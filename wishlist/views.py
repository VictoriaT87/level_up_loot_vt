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
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you need to be logged in to add your Wishlist.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user=user.user)
    products = Product.objects.all()

    template = 'wishlist/wishlist.html'

    context = {
        'products': products,
        'wishlist': wishlist,
    }
    
    return render(request, template, context)


@login_required
def add_wishlist(request, product_id):
    """
    Add a view to show the wishlist
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Please log in to add items to your Wishlist.')
        return redirect(reverse('account_login'))
        
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    
    already_added = Wishlist.objects.filter(product=product,
                                       user=user.user).exists()
    if already_added:
        messages.info(request, f'{product.title} is already in your Wishlist!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        Wishlist.objects.create(user=user.user, product=product)
    messages.success(request,
                     f'{product.title} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_wishlist(request, product_id):
    """
    Remove an item from the wishlist
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Please log in to remove items from your Wishlist.')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.filter(product=product,
                                       user=user.user).delete()
    messages.info(request,
                  f'{product.title} has been removed from your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))
