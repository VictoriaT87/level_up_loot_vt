from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm


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
