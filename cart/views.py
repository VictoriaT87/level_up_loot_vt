from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a quantity of the chosen product
    to the shopping cart
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    item = f'{item_id}'
    cart = request.session.get('cart', {})

    if item in list(cart.keys()):
        cart[item] += quantity
        messages.success(request, f'Added {product.title}')
    else:
        cart[item] = quantity
        messages.success(request, f'Added {product.title}')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
