from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """
    Add a quantity of the chosen product
    to the shopping cart
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    item = f"{item_id}"
    cart = request.session.get("cart", {})

    if item in list(cart.keys()):
        cart[item] += quantity
        messages.success(request, f"Added {product.title}")
    else:
        cart[item] = quantity
        messages.success(request, f"Added {product.title}")

    request.session["cart"] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        # update quantity
        cart[item_id] = quantity
        messages.success(
            request, (f"Updated {product.title} " f"quantity to {cart[item_id]}")
        )
    else:
        # delete item by pop function
        cart.pop(item_id)
        messages.success(request, (f"Removed {product.title} " f"from your cart"))

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


def remove_from_cart(request, item_id):
    """Remove an item from the shopping cart"""

    product = Product.objects.get(pk=item_id.split("_")[0])
    cart = request.session.get("cart", {})

    try:
        cart.pop(item_id)
        messages.success(request, f"Removed {product.title}")

        request.session["cart"] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
