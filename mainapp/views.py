from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from .models import *
# from .mixins import CategoryDetailMixin


class IndexView(ListView):
    model = Category
    template_name = 'index.html'


class ShopView(ListView):
    model = Jacket
    template_name = 'shop.html'

# def show_category(request, cat_id):
#     post = get_object_or_404(Category, pk=cat_id)
#
#     context = {
#         'posts': post,
#     }
#     return render(request, 'shop.html', context=context)
# category = Category.objects.all()
# objects = Jacket.objects.all()
# context = {
#     'category': category,
#     'objects': objects
# }
#
#
# def index_view(request):
#     return render(request, 'index.html', context)
#
#
# def shop_view(request):
#     return render(request, 'shop.html', context)
#
#
# def single_product_details_view(request):
#     return render(request, 'single-product-details.html', context)
#
#
# def checkout_view(request):
#     return render(request, 'checkout.html', context)
#
#
# def regular_page_view(request):
#     return render(request, 'regular-page.html', context)
#
#
# def contact_view(request):
#     return render(request, 'contact.html', context)
