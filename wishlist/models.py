from django.db import models

from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Wishlist(models.Model):
    """ A model for a user's wishlist """
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE, default=1)
    # automatically create and add date when a review is added
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f"{self.user.first_name}'s Wishlist"