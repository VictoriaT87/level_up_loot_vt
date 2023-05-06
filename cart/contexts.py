from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    # get cart session
    cart = request.session.get('cart', {})

    # for each item id and the quantity in cart session
    for item_id, item_data in cart.items():
        # if the item_data is an integer, it doesn't have a
        # dictionary, so doesn't have a size
        if isinstance(item_data, int):
            # get the product
            product = get_object_or_404(Product, pk=item_id)
            # total is quantity times the price
            total += item_data * product.price
            # incremenet product count is quantity
            product_count += item_data
            # append the cart with each context
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            # iterate through the dictionary with sizes
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # id the total price is less than the free delivery price in settings
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # delivery = total price times decimal percentage of delivery price
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # delivery is total minus the threshold price
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # else delivery is free
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return 