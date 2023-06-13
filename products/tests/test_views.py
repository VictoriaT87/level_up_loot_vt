from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product, Category, Brand
from products.views import all_products, product_detail, add_product, edit_product, delete_product

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
            username='superuser',
            password='testpw',
            email='superuser@example.com'
        )
        testsuperuser.save()

        # Create test brand and category
        self.category = Category.objects.create(name='Gaming')
        self.brand = Brand.objects.create(name='Sideshow')

        # https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
        image_file = SimpleUploadedFile(
            name='box.png',
            content=open('media/box.png', 'rb').read(),
            content_type='image/png'
        )

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku='123456',
            description="Test description",
            price='9.99',
            image=image_file,
        )

    def test_can_get_products_page(self):
        # Assert that the products page template is used correctly
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_all_products_with_search_query(self):
        # Test all products with empty search query
        response = self.client.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "You didn't enter any search criteria!")

    def test_can_get_all_products_from_search(self):
        # Test retrieving all products with a search term
        response = self.client.get('/products/', {'search_term': 'anime', })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort(self):
        # Test sorting products by title in descending order
        response = self.client.get('/products/', {'sort': 'title',
                                   'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_add_product_page(self):
        # Test accessing the add product page when logged in as a superuser
        logged_in = self.client.login(username='superuser',
                                      password='testpw')
        self.assertTrue(logged_in)
        testsuperuser = User.objects.get(username='superuser')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')


class ProductDetailTest(TestCase):
    """
    Test Product Details View
    """

    def setUp(self):
        # Create Superuser
        testsuperuser = User.objects.create_superuser(
            username='superuser',
            password='testpw',
        )
        testsuperuser.save()

        # Create test brand and category
        self.category = Category.objects.create(name='Gaming')
        self.brand = Brand.objects.create(name='Sideshow')

        # https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
        image_file = SimpleUploadedFile(
            name='box.png',
            content=open('media/box.png', 'rb').read(),
            content_type='image/png'
        )

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku='123456',
            description="Test description",
            price='9.99',
            image=image_file,
        )

    def test_product_detail_view(self):
        # Test the product detail page renders as expected
        client = Client()
        url = reverse('product_detail', args=[self.product.id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'products/product_detail.html')

        # Assert that the product details are present in the response
        self.assertContains(response, self.product.title)
        self.assertContains(response, self.product.description)

        # Assert that the related products are passed to the template
        self.assertIn('related_products', response.context)

        # Assert that if wishlist is in the user's session, IsNotNone. Otherwise None.
        wishlist = response.context.get('wishlist')
        if client.session.get('wishlist'):
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
            username='superuser',
            password='testpw',
        )
        self.client.login(username='superuser', password='testpw')

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku='123456',
            description="Test description",
            price='9.99',
        )

    def test_edit_product_view_as_superuser(self):
        # Test Delete Product View

        # Get the URL for the delete_product view with the product ID
        url = reverse('edit_product', args=[self.product.id])
        self.client.login(username='superuser', password='testpw')
        
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'products/edit_product.html')


    def test_edit_product_view_as_non_superuser(self):
        # Test Edit Product View when not Superuser

        # Create User
        self.user = User.objects.create_user(
            username='regularuser',
            password='testpw',
        )
        self.client.force_login(self.user)

        url = reverse('edit_product', args=[self.product.id])
        response = self.client.post(url)

        # Assert that the response is a redirect to the home page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

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
            username='superuser',
            password='testpw',
        )
        self.client = Client()

        # Create test product
        self.product = Product.objects.create(
            title="Test Product",
            sku='123456',
            description="Test description",
            price='9.99',
        )

    def test_delete_product_view_as_superuser(self):
        # Test Delete Product View

        # Get the URL for the delete_product view with the product ID
        url = reverse('delete_product', args=[self.product.id])
        self.client.force_login(self.superuser)

        response = self.client.post(url)

        # Assert that the response is a redirect to the products page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products'))

        # Verify that the product is deleted
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())


    def test_delete_product_not_superuser(self):
        # Test Delete Product View when not Superuser

        # Create User
        self.user = User.objects.create_user(
            username='regularuser',
            password='testpw',
        )
        self.client.force_login(self.user)

        url = reverse('delete_product', args=[self.product.id])
        response = self.client.post(url)

        # Assert that the response is a redirect to the home page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # Assert that the error message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners can do that.")