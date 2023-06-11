from django.test import TestCase
from products.models import Category, Brand

class CategoryModelTest(TestCase):
    """
    Test Category Model
    """
    @classmethod
    def setUpTestData(cls):
        # Setup new Category to test
        Category.objects.create(name='Test Category', friendly_name='Friendly Test Category')

    def test_name_field(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_friendly_name_field(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('friendly_name').verbose_name
        self.assertEquals(field_label, 'friendly name')

    def test_str_method(self):
        category = Category.objects.get(id=1)
        expected_str = category.name
        self.assertEquals(str(category), expected_str)

    def test_get_friendly_name_method(self):
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
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_friendly_name_field(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('friendly_name').verbose_name
        self.assertEquals(field_label, 'friendly name')

    def test_str_method(self):
        brand = Brand.objects.get(id=1)
        expected_str = brand.name
        self.assertEquals(str(brand), expected_str)

    def test_get_friendly_name_method(self):
        brand = Brand.objects.get(id=1)
        expected_friendly_name = brand.friendly_name
        self.assertEquals(brand.get_friendly_name(), expected_friendly_name)