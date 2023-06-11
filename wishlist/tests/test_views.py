from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.urls import reverse
from profiles.models import UserProfile
from wishlist.models import Wishlist
from wishlist.views import view_wishlist


class WishlistViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Create a user
        """
        super().setUpClass()
        cls.client = Client()
        cls.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_authenticated_user_view_wishlist(self):
        # Create a UserProfile if it doesn't exist
        user_profile = UserProfile.objects.get_or_create(user=self.user)

        # Create a wishlist for the user
        wishlist = Wishlist.objects.create(user=self.user)

        # Log in the user using the client
        self.client.login(username='testuser', password='testpass')

        # Make a GET request to the wishlist view
        response = self.client.get(reverse('wishlist'))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

        # Assert that the wishlist object is passed to the template context
        self.assertEqual(response.context['wishlist'], wishlist)


    def test_unauthenticated_user_view_wishlist(self):
        # User is none (not logged in/authorized)
        user = None

        # Make a GET request to the wishlist view
        response = self.client.get(reverse('wishlist'))

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the login page
        self.assertRedirects(response, reverse('account_login'))

        # Assert that an error message is shown
        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727#14909727
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Sorry, you need to be logged in to add your Wishlist.', messages)
