from django.test import TestCase
from django.urls import reverse

from products.forms import ProductForm, ReviewsForm
from products.models import Category, Brand, Product


class ProductFormTest(TestCase):
    """
    Test Product Form
    """

    def test_form_fields(self):
        # Test form fields
        form = ProductForm()
        self.assertEqual(form.Meta.model, Product)
        self.assertEqual(form.Meta.fields, "__all__")
        self.assertEqual(form.Meta.exclude, ("created_on",))

    def test_form_choices(self):
        # Test form choices
        category = Category.objects.create(name="Category")
        brand = Brand.objects.create(name="Brand")

        form = ProductForm()
        self.assertEqual(
            form.fields["category"].choices,
            [(category.id, category.get_friendly_name())],
        )
        self.assertEqual(
            form.fields["brand"].choices, [(brand.id, brand.get_friendly_name())]
        )

    def test_form_is_valid(self):
        # Assert Form is Valid

        category = Category.objects.create(name="Category")
        brand = Brand.objects.create(name="Brand")

        form_data = {
            "category": category.pk,
            "brand": brand.pk,
            "sku": "123456",
            "title": "Test Product",
            "alt_text": "Alt text",
            "description": "Test description",
            "price": "9.99",
            "average_rating": "4.5",
            "is_featured": True,
            "on_sale": False,
            "sale_price": "0.00",
            "discount": 0,
            "discounted_price": 0,
        }

        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        # Assert Form is Invalid

        category = Category.objects.create(name="Category")
        brand = Brand.objects.create(name="Brand")

        form_data = {
            "category": category.pk,
            "brand": brand.pk,
            "sku": "123456",
            "title": "",
            "alt_text": "Alt text",
            "description": "Test description",
            "price": "9.99",
            "average_rating": "4.5",
            "is_featured": True,
            "on_sale": False,
            "sale_price": "0.00",
            "discount": 0,
            "discounted_price": 0,
        }

        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())


class ReviewsFormTest(TestCase):
    """
    Test Review Form
    """

    def test_reviews_form_valid(self):
        # Assert review is valid
        form_data = {
            "title": "Great product",
            "review": "This is a fantastic product. Highly recommended.",
        }
        form = ReviewsForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_reviews_form_invalid(self):
        # Assert review is invalid
        form_data = {
            "title": "",
            "review": "",
        }
        form = ReviewsForm(data=form_data)
        self.assertFalse(form.is_valid())
