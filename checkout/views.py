from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from cart.contexts import cart_contents

# Create your views here.


def checkout(request):

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            # from context processer
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    # if item is integer, doesn't have size
                    isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                # if item doesn't exist
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # if user wants to save their data
            request.session['save_info'] = 'save-info' in request.POST
            # return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('products'))

        # get current cart total from context.py
        current_cart = cart_contents(request)
        # get grand_total key from cart in context.py
        total = current_cart['grand_total']
        # round function to get integer
        # stripe_total = round(total * 100)
        # stripe.api_key = stripe_secret_key
        # intent = stripe.PaymentIntent.create(
        #     amount=stripe_total,
        #     currency=settings.STRIPE_CURRENCY,
        # )

        # Attempt to prefill the form with any info the user maintains in their profile
    #     if request.user.is_authenticated:
    #         try:
    #             profile = UserProfile.objects.get(user=request.user)
    #             order_form = OrderForm(initial={
    #                 'full_name': profile.user.get_full_name(),
    #                 'email': profile.user.email,
    #                 'phone_number': profile.default_phone_number,
    #                 'country': profile.default_country,
    #                 'postcode': profile.default_postcode,
    #                 'town_or_city': profile.default_town_or_city,
    #                 'street_address1': profile.default_street_address1,
    #                 'street_address2': profile.default_street_address2,
    #                 'county': profile.default_county,
    #             })
    #         except UserProfile.DoesNotExist:
    #             order_form = OrderForm()
    #     else:
    #         order_form = OrderForm()

    # if not stripe_public_key:
    #     messages.warning(request, 'Stripe public key is missing. \
    #         Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
