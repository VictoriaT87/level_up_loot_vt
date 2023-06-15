from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from checkout.models import Coupon


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
