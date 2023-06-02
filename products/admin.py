from django.contrib import admin
from .models import Product, Category, Brand

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # search by username
    search_fields = ['title',]
    list_display = (
        'title',
        'sku',
        'category',
        'brand',
        'price',
        'image',
        'on_sale',
        'sale_price',
        'is_featured',
    )

    list_editable = ('is_featured', 'on_sale',)

    ordering = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
