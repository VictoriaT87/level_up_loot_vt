from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from wishlist.models import Wishlist

class WishlistModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test User
        user = User.objects.create(username='testuser')
        # Create a test product
        product = Product.objects.create(
            title="Test Product",
            description="Test description",
            price='9.99',
        )

        # Create a test Wishlist
        Wishlist.objects.create(user=user, date_added='2023-06-01')

        # Add the product to the wishlist
        wishlist = Wishlist.objects.get(user=user)
        wishlist.products.add(product)

    def test_string_representation(self):
        # test the returned string
        wishlist = Wishlist.objects.get(id=1)
        expected_str = f"{wishlist.user.username}'s Wishlist"
        self.assertEqual(str(wishlist), expected_str)

    def test_products_many_to_many_relationship(self):
        # test that the wishlist has a product in it
        wishlist = Wishlist.objects.get(id=1)
        products = wishlist.products.all()
        self.assertEqual(len(products), 1)

    def test_user_one_to_one_relationship(self):
        # test that the user is not none and has the expected username
        wishlist = Wishlist.objects.get(id=1)
        user = wishlist.user
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_date_added_field(self):
        # test the date added field
        wishlist = Wishlist.objects.get(id=1)
        date_added = wishlist.date_added
        self.assertIsNotNone(date_added)