from django.shortcuts import render
from django.views.generic import ListView
from .models import *


category = Category.objects.all()


# Create your views here.
def index_view(request):
    return render(request, 'index.html', {'category': category})


def shop_view(request):
    return render(request, 'shop.html', {'category': category})


def single_product_details_view(request):
    return render(request, 'single-product-details.html', {})


def checkout_view(request):
    return render(request, 'checkout.html', {})


def regular_page_view(request):
    return render(request, 'regular-page.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})



