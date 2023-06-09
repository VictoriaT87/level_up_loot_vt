from django.test import TestCase
from profiles.forms import UserProfileForm
from django.contrib.auth.models import User


class UserProfileFormTest(TestCase):
    """
    Tests for the UserProfile Form
    """

    def test_form_fields(self):
        # Test field names
        form = UserProfileForm()
        fields = [
            "name",
            "default_phone_number",
            "default_postcode",
            "default_town_or_city",
            "default_street_address1",
            "default_street_address2",
            "default_county",
        ]
        for field_name in fields:
            self.assertIn(field_name, form.fields)

    def test_form_placeholders(self):
        # Test placeholders
        form = UserProfileForm()
        expected_attrs = {
            "default_phone_number": {"autofocus": True},
            "name": {"placeholder": "Your Name"},
            "default_phone_number": {"placeholder": "Phone Number"},
            "default_postcode": {"placeholder": "Postal Code"},
            "default_town_or_city": {"placeholder": "Town or City"},
            "default_street_address1": {"placeholder": "Street Address 1"},
            "default_street_address2": {"placeholder": "Street Address 2"},
            "default_county": {"placeholder": "County, State or Locality"},
        }

    def test_form_label(self):
        # Test form labels
        form = UserProfileForm()
        for field_name, field in form.fields.items():
            self.assertFalse(field.label)

    def test_form_is_valid(self):
        # Test Form is Valid
        form_data = {
            "full_name": "Test User",
            "email": "testuser@email.com",
            "phone_number": "12345678",
            "country": "IE",
            "postcode": "12345",
            "town_or_city": "Dublin",
            "street_address1": "Street",
            "county": "Dublin",
        }

        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        # Test Form is Invalid
        form_data = {
            "full_name": "",
            "email": "testuser@email.com",
            "phone_number": "12345678",
            "country": "IE",
            "postcode": "12345",
            "town_or_city": "Dublin",
            "street_address1": "Street",
            "county": "Dublin",
        }

        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())
