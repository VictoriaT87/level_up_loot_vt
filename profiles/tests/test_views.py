from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from profiles.models import UserProfile
from profiles.views import profile, order_history, DeleteProfile
from profiles.forms import UserProfileForm
from checkout.models import Order
from django.urls import reverse
from django.shortcuts import get_object_or_404


class TestProfilesViews(TestCase):
    """ Tests for profiles app views """

    def setUp(self):
        # Setup Test User
        testuser = User.objects.create_user(
            username='test_username',
            password='secret',
            email='testuser@email.com'
        )
        testuser.save()

    def test_get_profile_page(self):
        # User can view profile page with GET
        self.client.login(username='test_username', password='secret')

        # Make a GET request to the profile view
        response = self.client.get(reverse('profile'))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'profiles/profile.html')


    def test_post_profile_page(self):
        # User can view profile page with POST
        self.client.login(username='test_username', password='secret')

        # Make a POST request to the profile view
        response = self.client.post(reverse('profile'))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'profiles/profile.html')


    def test_unauthorized_post_profile_page(self):
        # User is not logged in
        response = self.client.post(reverse('profile'))

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the login page
        expected_url = f"{reverse('account_login')}?next={reverse('profile')}"
        self.assertRedirects(response, expected_url)


class OrderHistoryViewTest(TestCase):
    """ Tests for order history """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        # Setup Test Order
        self.order = Order.objects.create(
            order_number='1234567890',
            user_profile=UserProfile.objects.get(user=self.user),
            full_name='Test User',
            email='testuser@email.com',
            phone_number='12345678',
            country='IE',
            postcode='12345',
            town_or_city='Dublin',
            street_address1='My Street',
            county='Anywhere',
        )

    def test_order_history_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Make a GET request to the order history view
        response = self.client.get(reverse('order_history', args=['1234567890']))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

        # Assert that the order instance is correctly passed to the context
        order = response.context['order']
        self.assertEqual(order, self.order)

        # Assert that the correct message is added to the messages framework
        messages = [m.message for m in get_messages(response.wsgi_request)]
        expected_message = f'This is a past confirmation for order number {self.order.order_number}. A confirmation email was sent on the order date.'
        self.assertIn(expected_message, messages)


class DeleteProfileViewTest(TestCase):
    """ Tests for DeleteProfile view """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        self.profile = self.user.userprofile

    def test_delete_profile(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Make a POST request to delete the profile
        response = self.client.post(reverse('user-delete', kwargs={'pk': self.profile.pk}))

        # Assert that the response is a redirect
        self.assertRedirects(response, reverse('home'))

        # Assert that the user is deleted
        self.assertFalse(User.objects.filter(username='testuser').exists())

        # Assert that the success message is added to the messages framework
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Profile successfully deleted', messages)