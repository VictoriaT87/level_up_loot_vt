from django.test import TestCase
from products.models import Category, Brand, Product, Reviews

import decimal
from decimal import Decimal

class CategoryModelTest(TestCase):
    """
    Test Category Model
    """

    @classmethod
    def setUpTestData(cls):
        # Setup new Category to test
        Category.objects.create(name='Test Category', friendly_name='Friendly Test Category')

    def test_name_field(self):
        # Test the name field label
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_friendly_name_field(self):
        # Test the friendly_name field label
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('friendly_name').verbose_name
        self.assertEquals(field_label, 'friendly name')

    def test_str_method(self):
        # Test the __str__ method
        category = Category.objects.get(id=1)
        expected_str = category.name
        self.assertEquals(str(category), expected_str)

    def test_get_friendly_name_method(self):
        # Test the get_friendly_name method
        category = Category.objects.get(id=1)
        expected_friendly_name = category.friendly_name
        self.assertEquals(category.get_friendly_name(), expected_friendly_name)


class BrandModelTest(TestCase):
    """
    Test Brand Model
    """

    @classmethod
    def setUpTestData(cls):
        # Setup new Brand to test
        Brand.objects.create(name='Test Brand', friendly_name='Friendly Test Brand')

    def test_name_field(self):
        # Test the name field label
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_friendly_name_field(self):
        # Test the friendly_name field label
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('friendly_name').verbose_name
        self.assertEquals(field_label, 'friendly name')

    def test_str_method(self):
        # Test the __str__ method
        brand = Brand.objects.get(id=1)
        expected_str = brand.name
        self.assertEquals(str(brand), expected_str)

    def test_get_friendly_name_method(self):
        # Test the get_friendly_name method
        brand = Brand.objects.get(id=1)
        expected_friendly_name = brand.friendly_name
        self.assertEquals(brand.get_friendly_name(), expected_friendly_name)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up test Product  
        category = Category.objects.create(name='Category')
        brand = Brand.objects.create(name='Brand')
        Product.objects.create(
            category=category,
            brand=brand,
            sku='123456',
            title='Test Product',
            alt_text='Test Alt Text',
            description='Test Description',
            price=9.99,
            average_rating=4.5,
            is_featured=True,
            on_sale=True,
            discount=20,
        )

    def test_product_fields(self):
        # Test all fields are correctly filled
        product = Product.objects.get(id=1)
        self.assertEqual(product.category.name, 'Category')
        self.assertEqual(product.brand.name, 'Brand')
        self.assertEqual(product.sku, '123456')
        self.assertEqual(product.title, 'Test Product')
        self.assertEqual(product.alt_text, 'Test Alt Text')
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.price, Decimal('9.99'))
        self.assertEqual(product.average_rating, 4.5)
        self.assertTrue(product.is_featured)
        self.assertTrue(product.on_sale)
        self.assertEqual(product.discount, 20)