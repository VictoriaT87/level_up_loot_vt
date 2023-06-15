from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your models here.


class Category(models.Model):
    """Model for all categories"""

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """Model for all brands"""

    class Meta:
        verbose_name_plural = "Brands"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Model for all products"""

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    brand = models.ForeignKey("Brand", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    alt_text = models.CharField(max_length=254, default="alt text")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    average_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image = models.ImageField(null=True, blank=True)
    is_featured = models.BooleanField(
        default=False, verbose_name="Feature on Home Page"
    )
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=4, decimal_places=2)
    discount = models.IntegerField(
        default=10,
        help_text="Discount in Percentage",
        verbose_name="Discount If Product On Sale",
    )
    discounted_price = models.IntegerField(null=True)
    created_on = models.DateField(default=timezone.now)

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

    @property
    def discounted_price(self):
        return ((self.price) * (self.discount)) / 100

    @property
    def sale_price(self):
        return (self.price) - (self.discounted_price)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    """Model for product reviews"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "product"], name="reviews_per_user")
        ]

    def __str__(self):
        return self.title
