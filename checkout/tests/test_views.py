from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404
from datetime import date
from checkout.models import Coupon, Order


class AddCouponViewTest(TestCase):
    """ Test Add Coupon View """

    def setUp(self):
        self.client = Client()

        # Create coupon
        self.coupon = Coupon.objects.create(
            code='test',
            discount=10.0,
            active=True,
            start_date=date.today(),
            expiry_date=date.today(),
        )

    def test_add_valid_coupon(self):
        # Test Add Valid Coupon

        # Add the coupon
        response = self.client.post(
            reverse('add_coupon'), {'code': 'test'})

        # Assert the coupon ID is in the session storage
        coupon = get_object_or_404(Coupon, code='test')
        self.assertEqual(self.client.session.get('coupon_id'), coupon.id)

        # Check the message returned
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f'Coupon code: test applied')

    def test_add_wrong_coupon(self):
        # Test Add Wrong Coupon

        # Add the wrong coupon
        response = self.client.post(reverse('add_coupon'), {'code': 'wrong'})

        # Assert the coupon ID is not in the session storage
        self.assertIsNone(self.client.session.get('coupon_id'))

        # Check the message returned
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f'Sorry, wrong is not a valid code')


class RemoveCouponViewTest(TestCase):
    """ Test Remove Coupon View """

    def setUp(self):
        self.client = Client()

        # Create coupon
        self.coupon = Coupon.objects.create(
            code='test',
            discount=10.0,
            active=True,
            start_date=date.today(),
            expiry_date=date.today(),
        )

    def test_remove_coupon(self):
        # Test Remove Coupon

        # Add the coupon ID to the session
        self.client.session['coupon_id'] = 1

        # Make a POST request to remove the coupon
        response = self.client.post(reverse('remove_coupon'))

        # Assert the coupon ID is removed from the session
        self.assertIsNone(self.client.session.get('coupon_id'))

        # Check the message returned
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "The coupon has been removed")


class CheckoutViewTest(TestCase):
    """ Test Checkout View """

    def test_empty_cart(self):
        # Test Checkout View with an Empty Cart

        # Create empty cart
        self.client.session['cart'] = {}

        # Call the view
        response = self.client.get(reverse('checkout'))

        # Check the messages in the response
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your cart at the moment")


class CheckoutSuccessViewTest(TestCase):
    """ Test Checkout Success View """

    def setUp(self):
        # Setup Client
        self.client = Client()

        # Setup Order
        self.order = Order.objects.create(
            order_number='12345',
            email='test@test.com'
        )

    def test_checkout_success_view(self):
        # Test Checkout Success View Template and Message

        response = self.client.get(reverse('checkout_success', args=['12345']))
        self.assertEqual(response.status_code, 200)

        # Assert that the email message sent
        messages = [str(message)
                    for message in get_messages(response.wsgi_request)]
        self.assertIn(
            f'Order successfully processed! \
        Your order number is {self.order.order_number}. A confirmation \
        email will be sent to {self.order.email}.', messages)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
