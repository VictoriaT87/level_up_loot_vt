from django.test import TestCase
from django.urls import reverse

from checkout.models import Order
from checkout.forms import OrderForm


class OrderFormTest(TestCase):
    """
    Test Order Form
    """

    def test_form_fields(self):
        # Test form fields
        form = OrderForm()
        self.assertEqual(form.Meta.model, Order)
        self.assertEqual(
            list(form.Meta.fields),
            ['full_name', 'email', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'postcode', 'country', 'county']
        )

    def test_form_placeholders(self):
        # Test form choices
        form = OrderForm()
        self.assertEqual(
            form.fields['full_name'].widget.attrs['placeholder'], 'Full Name *')
        self.assertEqual(
            form.fields['email'].widget.attrs['placeholder'], 'Email Address *')
        self.assertEqual(
            form.fields['phone_number'].widget.attrs['placeholder'], 'Phone Number *')

    def test_form_is_valid(self):
        # Test Form is Valid
        form_data = {
            'full_name': 'Test User',
            'email': 'testuser@email.com',
            'phone_number': '12345678',
            'street_address1': 'Street',
            'street_address2': '',
            'town_or_city': 'Dublin',
            'postcode': '12345',
            'country': 'IE',
            'county': 'Dublin',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())