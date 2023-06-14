from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from products.models import Product
from cart.views import view_cart, add_to_cart


class CartViewTest(TestCase):
    """ Test Cart View """

    def test_view_cart(self):
        response = self.client.get(reverse('view_cart'))

        # Assert that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used to render the response
        self.assertTemplateUsed(response, 'cart/cart.html')


class AddToCartViewTest(TestCase):
    """ Test Add to Cart View """

    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username='regularuser',
            password='testpw',
        )
        self.client.force_login(self.user)

        # Create a test product
        self.product = Product.objects.create(title='Test Product', price=9.99)

    def test_add_to_cart(self):
        # Define the URL for adding a product to the cart
        url = reverse('add_to_cart', args=[self.product.id])

        # Define the form data for adding the product
        form_data = {
            'quantity': 2,
            'redirect_url': reverse('product_detail', args=[self.product.id])
        }

        # Send a POST request to add the product to the cart
        response = self.client.post(url, data=form_data)

        # Assert that the response redirects to the correct URL
        self.assertRedirects(response, reverse(
            'product_detail', args=[self.product.id]))

        # Assert that the cart in the session has been updated
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)], 2)

        # Assert that the success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f'Added {self.product.title}')


class AdjustCartTest(TestCase):
    """ Test Adjusting Items in Cart """

    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username='regularuser',
            password='testpw',
        )
        self.client.force_login(self.user)

        # Create a test product
        self.product = Product.objects.create(title='Test Product', price=9.99)

    def test_adjust_cart(self):
        # Test Adjust Cart View

        # Define the form data for adjusting the cart
        form_data = {
            'quantity': 3,
        }

        # Send a POST request to adjust the cart
        response = self.client.post(
            reverse('adjust_cart', args=[self.product.id]), data=form_data)

        # Assert that the response is successful
        self.assertEqual(response.status_code, 302)

        # Assert that the cart in the session has been updated
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)], 3)

        # Assert that the success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Updated {self.product.title} quantity to 3')


class RemoveFromCartTest(TestCase):
    """ Test Remove From Cart View """

    def setUp(self):
        # Create a test product
        self.product = Product.objects.create(title='Test Product', price=9.99)

    def test_can_remove_product_from_cart(self):
        # Test remove_from_cart View

        # Add the product to the cart
        self.client.post(
            f'/cart/add/{str(self.product.id)}/',
            {'quantity': 2, 'redirect_url': 'view_cart'}
        )

        # Reload the cart page to clear any existing messages
        self.client.get(reverse('view_cart'))

        # Remove the product from the cart
        response = self.client.post(f'/cart/remove/{str(self.product.id)}/')

        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)

        # Assert that the success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f'Removed {self.product.title}')
