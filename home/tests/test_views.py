from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
from products.models import Product


class HomeViewTest(TestCase):
    """
    Tests for viewing the index page
    """
    def test_home_view(self):
        # Create some products for testing
        Product.objects.create(title='Product 1', description='Description 1', price=9.99)
        Product.objects.create(title='Product 2', description='Description 2', price=19.99)

        # Make a GET request to the index view
        response = self.client.get(reverse('home'))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'home/index.html')

        # Assert that the products are passed to the template context
        products = response.context['products']
        self.assertEqual(products.count(), 2)


class FAQsViewTest(TestCase):
    """
    Tests for viewing the FAQ page
    """
    def test_faqs_view(self):
        # Make a GET request to the FAQs view
        response = self.client.get(reverse('faqs'))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'home/faqs.html')


class PrivacyPolicyViewTest(TestCase):
    """
    Tests for viewing the Privacy Policy page
    """
    def test_privacy_policy_view(self):
        # Make a GET request to the privacy policy view
        response = self.client.get(reverse('privacy_policy'))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'home/privacy_policy.html')


class ContactViewTest(TestCase):
    """
    Tests for the Contact Page
    """
    def test_contact_view_get(self):
        # Make a GET request to the contact view
        response = self.client.get(reverse('contact'))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'home/contact.html')

    
    def test_contact_view_post(self):
        # Make a POST request to the contact view
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@test.com',
            'message': 'Hello, this is a test message.'
        })

        # Assert that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Assert that the email has been sent
        # https://stackoverflow.com/questions/35364161/how-to-test-send-mail-in-django
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'message from Test User')
        self.assertIn('Hello, this is a test message.', mail.outbox[0].body)

        # Assert that the success message is displayed
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Thank you, your email has been sent. We will contact you shortly.', messages)
