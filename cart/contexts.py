from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.contrib import messages
from django.shortcuts import get_object_or_404
from checkout.models import Coupon


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})
    coupon_id = request.session.get("coupon_id", int())

    try:
        coupon = Coupon.objects.get(id=coupon_id)

    except Coupon.DoesNotExist:
        coupon = None

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)

            # If product is on sale, show sale price
            if product.on_sale:
                price = product.sale_price
            else:
                price = product.price

            total += item_data * price
            product_count += item_data
            cart_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                    "price": price,
                }
            )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    if coupon:
        discount = total * Decimal(coupon.discount / 100)
        grand_total = total - discount + delivery
        stripe_total = round(grand_total * 100)
    else:
        discount = 0
        grand_total = delivery + total
        stripe_total = round(grand_total * 100)

    sub_total = total + delivery

    context = {
        "cart_items": cart_items,
        "coupon": coupon,
        "discount": discount,
        "total": total,
        "sub_total": sub_total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
