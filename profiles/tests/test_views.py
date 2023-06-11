from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from profiles.models import UserProfile
from profiles.views import profile
from profiles.forms import UserProfileForm
from checkout.models import Order
from django.urls import reverse


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

        # Setup Test Order
        Order.objects.create(
            order_number='1234567890',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='testuser@email.com',
            phone_number='12345678',
            country='IE',
            postcode='12345',
            town_or_city='Dublin',
            street_address1='My Street',
            county='Anywhere',
        )

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