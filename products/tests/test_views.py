from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product, Category, Brand

from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile

class AllProductsViewTest(TestCase):
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
        self.assertEqual(str(messages[0]), "You didn't enter any search criteria!")

    def test_can_get_all_products_from_search(self):
        # Test retrieving all products with a search term
        response = self.client.get('/products/', {'search_term': 'anime',})
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