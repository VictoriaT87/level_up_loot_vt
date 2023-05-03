from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Brand, Category
from .forms import ProductForm

import random


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()

    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

