from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Brand, Category, Reviews
from .forms import ProductForm, ReviewsForm

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
            category = request.GET['category']
            products = products.filter(category__name=category)
            category = get_object_or_404(Category, name=category)

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

    reviews = Reviews.objects.filter(
        product=product).order_by('-created_on')

    template = 'products/product_detail.html'
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure \
                the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please \
                ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_title = product.title
    product.delete()
    messages.info(request, f'{product_title} deleted')

    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a Product Review """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewsForm(request.POST)

        if review_form.is_valid():
            Reviews.objects.create(
                product=product,
                user=request.user,
                title=request.POST['title'],
                review=request.POST['review'],
            )
            reviews = Reviews.objects.filter(product=product)
            messages.success(
                request, 'Your review has been successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Your review has not been submitted')
    return redirect(reverse('product_detail', args=[product.id]))


class UpdateReview(LoginRequiredMixin,
                   SuccessMessageMixin, UpdateView):
    """
    A view to edit a Review
    """
    model = Reviews
    form_class = ReviewsForm
    template_name = "products/edit_review.html"
    success_message = "Your review was updated!"

    def get_success_url(self):
        return reverse('product_detail', kwargs={'product_id': self.object.product_id})


class DeleteReview(LoginRequiredMixin, DeleteView):
    """
    A view to delete a Review
    """
    model = Reviews
    template_name = "products/delete_review.html"
    success_message = "Review deleted successfully."
   
    def get_success_url(self):
        return reverse('product_detail', kwargs={'product_id': self.object.product_id})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteReview, self).delete(
            request, *args, **kwargs)