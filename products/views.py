from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Brand, Category
from .forms import ProductForm

import random


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    brand = None
    categories = None
    sale = False
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__name=categories)
            categories = get_object_or_404(Category, name=categories)

        if 'brand' in request.GET:
            brand = request.GET['brand']
            products = products.filter(brand__name=brand)
            brand = get_object_or_404(Brand, name=brand)

        if 'sale' in request.GET:
            sale = True
            products = products.filter(on_sale=True)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                               request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (Q(title__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)


    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'sale': sale,
        'brand': brand,
        'current_categories': categories,
        'current_sorting': current_sorting,
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

