from django.contrib import admin
from .models import Wishlist

# Register your models here.


class WishlistAdmin(admin.ModelAdmin):
    # search by username
    search_fields = [
        "user",
    ]
    # adds boxes side by side to allow removing/adding products in admin
    filter_horizontal = ("products",)
    list_display = (
        "user",
        "date_added",
    )

    ordering = ("user",)


admin.site.register(Wishlist, WishlistAdmin)
