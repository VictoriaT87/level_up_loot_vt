from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.urls import reverse
from profiles.models import UserProfile
from wishlist.models import Wishlist
from products.models import Product


"""
Originally wrote this using classmethods
From tutorial https://www.youtube.com/watch?v=_8qLxaWMdzE
Reverted to self setUp
More in README.md
"""


class ViewWishlistTest(TestCase):
    """
    Test for viewing a wishlist
    """

    def setUp(self):
        self.client = Client()

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_authenticated_user_view_wishlist(self):
        # Create a UserProfile if it doesn't exist
        user_profile = UserProfile.objects.get_or_create(user=self.user)

        # Create a wishlist for the user
        wishlist = Wishlist.objects.create(user=self.user)

        # Log in the user using the client
        self.client.login(username="testuser", password="testpass")

        # Make a GET request to the wishlist view
        response = self.client.get(reverse("wishlist"))

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, "wishlist/wishlist.html")

        # Assert that the wishlist object is passed to the template context
        self.assertEqual(response.context["wishlist"], wishlist)

    def test_unauthenticated_user_view_wishlist(self):
        # Make a GET request to the wishlist view
        response = self.client.get(reverse("wishlist"))

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the login page
        self.assertRedirects(response, reverse("account_login"))

        # Assert that an error message is shown
        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727#14909727
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Sorry, you need to be logged in to add to your Wishlist.", messages
        )


class AddWishlistTest(TestCase):
    """
    Test for adding to a wishlist
    """

    def setUp(self):
        self.client = Client()

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create a test product
        self.product = Product.objects.create(
            title="Test Product",
            description="Test description",
            price="9.99",
        )

    def test_authenticated_user_add_wishlist(self):
        # Create a UserProfile if it doesn't exist
        user_profile = UserProfile.objects.get_or_create(user=self.user)

        # Log in the user
        self.client.force_login(self.user)

        # Add something to the wishlist
        response = self.client.post(reverse("add_wishlist", args=[self.product.id]))

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the product detail page
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )

        # Assert that the product is added to the wishlist
        wishlist = Wishlist.objects.get(user=self.user)
        self.assertIn(self.product, wishlist.products.all())

        # Assert that the success message is displayed
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            f"{self.product.title} has been added to your Wishlist!", messages
        )

    def test_unauthenticated_user_view_wishlist(self):
        # Make a GET request to the wishlist view
        response = self.client.get(reverse("wishlist"))

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the login page
        self.assertRedirects(response, reverse("account_login"))

        # Assert that an error message is shown
        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727#14909727
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Sorry, you need to be logged in to add to your Wishlist.", messages
        )


class RemoveWishlistTest(TestCase):
    """
    Test for removing product from a wishlist
    """

    def setUp(self):
        """
        Create a user, product, and wishlist for testing
        """

        self.client = Client()

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create a test product
        self.product = Product.objects.create(
            title="Test Product",
            description="Test description",
            price="9.99",
        )
        self.wishlist = Wishlist.objects.create(user=self.user)
        self.wishlist.products.add(self.product)

    def test_remove_wishlist(self):
        # Log in the user
        self.client.force_login(self.user)

        # Make a POST request to remove the product from the wishlist
        response = self.client.post(reverse("remove_wishlist", args=[self.product.id]))

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected back to the wishlist page
        self.assertRedirects(response, reverse("wishlist"))

        # Assert that the product is removed from the wishlist
        self.assertFalse(self.wishlist.products.filter(pk=self.product.id).exists())

        # Assert that the success message is shown
        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727#14909727
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            f"{self.product.title} has been removed from your Wishlist!", messages
        )

    def test_remove_wishlist_unauthenticated_user(self):
        # Make a POST request to remove the product from the wishlist without logging in
        response = self.client.post(reverse("remove_wishlist", args=[self.product.id]))

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the login page
        self.assertRedirects(response, reverse("account_login"))

        # Assert that an error message is shown
        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727#14909727
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            "Sorry, you need to be logged in to edit your Wishlist.", messages
        )
