from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm, CouponForm
from .models import Order, OrderLineItem
from .models import Coupon

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json


def get_coupon(request, code):
    """Get a coupon code stored in the database"""
    # coupon code based on freeCodeCamp.org
    # credited in README
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("checkout")


def add_coupon(request):
    """Allow a user to add the coupon code"""

    code = request.POST.get("code")

    try:
        coupon = Coupon.objects.get(code=code)
        request.session["coupon_id"] = coupon.id
        messages.info(request, f"Coupon code: { code } applied")
    except Coupon.DoesNotExist:
        request.session["coupon_id"] = None
        messages.error(request, f"Sorry, { code } is not a valid code")
        return redirect("checkout")
    else:
        return redirect("checkout")


def remove_coupon(request):
    """Remove coupon code"""

    # Based on unit testing - remove coupon_id only if in session
    if "coupon_id" in request.session:
        del request.session["coupon_id"]
    messages.success(request, "The coupon has been removed")
    return redirect("checkout")


@require_POST
def cache_checkout_data(request):
    try:
        # get payment ID from client key split
        pid = request.POST.get("client_secret").split("_secret")[0]
        # setup stripe to modify pyment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # modify metadata with user, if they saved info, JSON dump of cart
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    coupon_form = CouponForm()

    if request.method == "POST":
        cart = request.session.get("cart", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            coupon = request.session.get("coupon_id")
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            # Assign the coupon to the order
            if coupon is not None:
                code = Coupon.objects.get(pk=coupon)
                order.coupon = code
                request.session["coupon_id"] = None

            # from context processer
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your cart wasn't found. "
                            "Please call us for assistance!"
                        ),
                    )
                    order.delete()
                    return redirect(reverse("view_cart"))

            # if user wants to save their data
            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )
    else:
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse("products"))

        # get current cart total from context.py
        current_cart = cart_contents(request)
        # get grand_total key from cart in context.py
        total = current_cart["grand_total"]

        discount = current_cart["discount"]

        # round function to get integer
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.name,
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "country": profile.default_country,
                        "postcode": profile.default_postcode,
                        "town_or_city": profile.default_town_or_city,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "county": profile.default_county,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing. \
            Did you forget to set it in your environment?",
        )

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
        "coupon_form": coupon_form,
        "discount": discount,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    # delete cart when checkout done
    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "discount": order.coupon.discount if order.coupon else None,
    }

    return render(request, template, context)
