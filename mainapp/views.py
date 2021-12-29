from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import *
from .mixins import CategoryDetailMixin


# category = Category.objects.all()


# Create your views here.
class IndexView(CategoryDetailMixin, View):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        products = LatestProducts.objects.get_products_for_main_page()
        context = {
            'category': category,
            'products': products
        }
        return render(request, 'index.html', context)


# def index_view(request):
#     return render(request, 'index.html', {'category': category})

# class ShopView(CategoryDetailMixin, DetailView):
#     model = Category
#     queryset = Category.objects.all()
#     context_object_name = 'category'
#     template_name = 'shop.html'
#     slug_url_kwarg = 'slug'
#     def get(self, request):
#         return render(request, 'shop.html')


def shop_view(request):
    return render(request, 'shop.html', {})


def single_product_details_view(request):
    return render(request, 'single-product-details.html', {})


def checkout_view(request):
    return render(request, 'checkout.html', {})


def regular_page_view(request):
    return render(request, 'regular-page.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})
