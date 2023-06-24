from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product, Category, Brand, Reviews
from products.views import (
    all_products,
    product_detail,
    add_product,
    edit_product,
    delete_product,
    add_review,
)

from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages
from urllib.parse import urlencode
from django.core.files.uploadedfile import SimpleUploadedFile


class AllProductsViewTest(TestCase):
    """
    Test All Products View
    """

    def setUp(self):
        # Create Superuser
        testsuperuser = User.objects.create_superuser(
            username="superuser", password="testpw", email="superuser@example.com"
        )
        testsuperuser.save()

        # Create test brand and category
        self.category = Category.objects.create(name="Gaming")
        self.brand = Brand.objects.create(name="Sideshow")

        # https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
        image_file = SimpleUploadedFile(
            name="box.webp",
            content=open("media/box.webp", "rb").read(),
            content_type="image/png",
        )

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
            image=image_file,
        )

    def test_can_get_products_page(self):
        # Assert that the products page template is used correctly
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_all_products_with_search_query(self):
        # Test all products with empty search query
        response = self.client.get("/products/", {"q": ""})
        self.assertRedirects(response, "/products/")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You didn't enter any search criteria!")

    def test_can_get_all_products_from_search(self):
        # Test retrieving all products with a search term
        response = self.client.get(
            "/products/",
            {
                "search_term": "anime",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_sort(self):
        # Test sorting products by title in descending order
        response = self.client.get("/products/", {"sort": "title", "direction": "desc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")


class AddProductTest(TestCase):
    """Test Add Product View"""

    def setUp(self):
        # Create Superuser
        self.user = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        self.client.login(username="superuser", password="testpw")

        # Create test brand and category
        self.category = Category.objects.create(name="Gaming")
        self.brand = Brand.objects.create(name="Sideshow")

    def test_add_product_view_as_superuser(self):
        # Test Adding a Product

        # Set up test image
        # https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
        image_file = SimpleUploadedFile(
            name="box.webp",
            content=open("media/box.webp", "rb").read(),
            content_type="image/png",
        )

        # Set up category and brand for test product
        category = Category.objects.get(pk=1)
        brand = Brand.objects.get(pk=1)

        # Create a valid product form
        form_data = {
            "category": category.pk,
            "brand": brand.pk,
            "sku": "123456",
            "title": "Test Product",
            "alt_text": "Alt text",
            "description": "Test description",
            "price": "9.99",
            "average_rating": "4.5",
            "image": image_file,
            "is_featured": True,
            "on_sale": False,
            "sale_price": "0.00",
            "discount": 0,
            "discounted_price": 0,
        }

        url = reverse("add_product")
        response = self.client.post(url, form_data)

        # Verify the response status code
        self.assertEqual(response.status_code, 302)

        # Verify that the product is created in the database
        self.assertTrue(Product.objects.filter(title="Test Product").exists())

        # Verify the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Successfully added product!")

        # Verify the redirect URL
        product = Product.objects.get(title="Test Product")
        self.assertRedirects(response, reverse("product_detail", args=[product.id]))

    def test_add_product_view_not_superuser(self):
        # Get the URL for adding a product
        url = reverse("add_product")

        # Create a non-superuser user and log in
        user = User.objects.create_user(username="regularuser", password="testpw")
        self.client.login(username="regularuser", password="testpw")

        # Send a POST request to add a product
        response = self.client.post(url)

        # Verify the response status code
        self.assertEqual(response.status_code, 302)

        # Verify that the product is not created in the database
        self.assertFalse(Product.objects.exists())

        # Verify the error message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")

        # Verify the redirect URL
        self.assertRedirects(response, reverse("home"))


class ProductDetailTest(TestCase):
    """
    Test Product Details View
    """

    def setUp(self):
        # Create Superuser
        testsuperuser = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        testsuperuser.save()

        # Create test brand and category
        self.category = Category.objects.create(name="Gaming")
        self.brand = Brand.objects.create(name="Sideshow")

        # https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
        image_file = SimpleUploadedFile(
            name="box.webp",
            content=open("media/box.webp", "rb").read(),
            content_type="image/png",
        )

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
            image=image_file,
        )

    def test_product_detail_view(self):
        # Test the product detail page renders as expected
        client = Client()
        url = reverse("product_detail", args=[self.product.id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, "products/product_detail.html")

        # Assert that the product details are present in the response
        self.assertContains(response, self.product.title)
        self.assertContains(response, self.product.description)

        # Assert that the related products are passed to the template
        self.assertIn("related_products", response.context)

        # Assert that if wishlist is in the user's session, IsNotNone. Otherwise None.
        wishlist = response.context.get("wishlist")
        if client.session.get("wishlist"):
            self.assertIsNotNone(wishlist)
        else:
            self.assertIsNone(wishlist)


class EditProductViewTest(TestCase):
    """
    Test Edit Product View
    """

    def setUp(self):
        # Create Superuser
        self.user = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        self.client.login(username="superuser", password="testpw")

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

    def test_edit_product_view_as_superuser(self):
        # Test Delete Product View

        # Get the URL for the delete_product view with the product ID
        url = reverse("edit_product", args=[self.product.id])
        self.client.login(username="superuser", password="testpw")

        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, "products/edit_product.html")

    def test_edit_product_view_as_non_superuser(self):
        # Test Edit Product View when not Superuser

        # Create User
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client.force_login(self.user)

        url = reverse("edit_product", args=[self.product.id])
        response = self.client.post(url)

        # Assert that the response is a redirect to the home page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

        # Assert that the error message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")


class DeleteProductViewTest(TestCase):
    """
    Test Delete Product View
    """

    def setUp(self):
        # Create Superuser
        self.superuser = User.objects.create_superuser(
            username="superuser",
            password="testpw",
        )
        self.client = Client()

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

    def test_delete_product_view_as_superuser(self):
        # Test Delete Product View

        # Get the URL for the delete_product view with the product ID
        url = reverse("delete_product", args=[self.product.id])
        self.client.force_login(self.superuser)

        response = self.client.post(url)

        # Assert that the response is a redirect to the products page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("products"))

        # Verify that the product is deleted
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_delete_product_not_superuser(self):
        # Test Delete Product View when not Superuser

        # Create User
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client.force_login(self.user)

        url = reverse("delete_product", args=[self.product.id])
        response = self.client.post(url)

        # Assert that the response is a redirect to the home page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

        # Assert that the error message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")


class AddReviewViewTest(TestCase):
    """
    Test Add Review View
    """

    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client = Client()

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

    def test_add_review_view_user(self):
        # Test Delete Product View as user

        url = reverse("add_review", args=[self.product.id])
        self.client.login(username="regularuser", password="testpw")

        # Create a valid review form
        form_data = {
            "title": "Test Review",
            "review": "This is a test review.",
        }

        # Send a POST request to add the review
        response = self.client.post(url, form_data)

        # Verify the response
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )

        # Verify that the review is added
        self.assertTrue(
            Reviews.objects.filter(product=self.product, user=self.user).exists()
        )

        # Verify the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your review has been successfully added!")

    def test_add_review_view_invalid_form(self):
        # Test Add Review invalid form

        url = reverse("add_review", args=[self.product.id])
        self.client.login(username="regularuser", password="testpw")

        # Create an invalid review form
        form_data = {
            "title": "",
            "review": "This is a test review.",
        }

        # Send a POST request with an invalid form
        response = self.client.post(url, form_data)

        # Verify the response
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", args=[self.product.id])
        )

        # Verify that the review is not added
        self.assertFalse(
            Reviews.objects.filter(product=self.product, user=self.user).exists()
        )

        # Verify the error message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your review has not been submitted.")


class UpdateReviewViewTest(TestCase):
    """
    Test Edit Review View
    """

    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client = Client()

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

        # Create test review
        self.review = Reviews.objects.create(
            product=self.product,
            user=self.user,
            title="Initial Title",
            review="Initial Review",
        )

    def test_update_review_view(self):
        # Test Update Review Valid Form

        url = reverse("update_review", kwargs={"pk": self.review.pk})
        self.client.login(username="regularuser", password="testpw")

        # Create a valid review form
        form_data = {
            "title": "Updated Title",
            "review": "Updated Review",
        }

        # Send a POST request to update the review
        response = self.client.post(url, form_data)

        # Verify the response
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("product_detail", kwargs={"product_id": self.product.id})
        )

        # Refresh the review from the database
        # https://stackoverflow.com/questions/68971787/unit-test-for-django-update-form
        self.review.refresh_from_db()

        # Verify that the review is updated
        self.assertEqual(self.review.title, "Updated Title")
        self.assertEqual(self.review.review, "Updated Review")

        # Verify the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Your review was updated!")

    def test_update_review_view_invalid_form(self):
        # Test the Update Review Invalid Form

        url = reverse("update_review", kwargs={"pk": self.review.pk})
        self.client.login(username="regularuser", password="testpw")

        # Create a valid review form
        form_data = {
            "title": "",
            "review": "Updated Review",
        }

        # Send a POST request with an invalid form
        response = self.client.post(url, form_data)

        # Verify the response status code
        self.assertEqual(response.status_code, 200)

        # Verify that the template used is the edit_review.html template
        self.assertTemplateUsed(response, "products/edit_review.html")

        # Refresh the review from the database
        self.review.refresh_from_db()

        # Verify that the review is not updated
        self.assertEqual(self.review.title, "Initial Title")
        self.assertEqual(self.review.review, "Initial Review")


class DeleteReviewViewTest(TestCase):
    """Test Delete Review view"""

    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpw",
        )
        self.client = Client()

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku="123456",
            description="Test description",
            price="9.99",
        )

        # Create test review
        self.review = Reviews.objects.create(
            product=self.product,
            user=self.user,
            title="Initial Title",
            review="Initial Review",
        )

        def test_delete_review_view(self):
            # Test the Delete Review View Works

            # Get the URL for deleting the review
            url = reverse("delete_review", kwargs={"pk": review.pk})

            # Send a POST request to delete the review
            response = self.client.post(url)

            # Verify the response status code
            self.assertEqual(response.status_code, 302)

            # Verify that the review is deleted
            self.assertFalse(Reviews.objects.filter(pk=self.review.pk).exists())

            # Verify the success message
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(str(messages[0]), "Review deleted successfully.")
