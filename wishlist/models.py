from django.db import models

from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Wishlist(models.Model):
    """ A model for a user's wishlist """
    # multiple products allowed on 1 wishlist/1 product allowed on multiple wishlists
    products = models.ManyToManyField(Product, blank=True)
    # user associated with only 1 wishlist
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"