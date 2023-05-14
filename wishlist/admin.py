from django.contrib import admin
from .models import Wishlist

# Register your models here.


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'date_added',
    )

    ordering = ('user',)

admin.site.register(Wishlist, WishlistAdmin)