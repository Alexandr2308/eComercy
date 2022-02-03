from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *


class IndexView(ListView):
    model = Product
    template_name = 'index.html'


class ShopView(ListView):
    model = Product
    template_name = 'shop.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'single-product-details.html'


# class CategoryListView(ListView):
#     model = Shorts
#     template_name = 'shop.html'



# def show_category(request, cat_id):
#     post = get_object_or_404(Category, pk=cat_id)
#
#     context = {
#         'posts': post,
#     }
#     return render(request, 'shop.html', context=context)
# category = Category.objects.all()
# objects = Shorts.objects.all()
# context = {
#     'category': category,
#     'objects': objects
# }


#
#
# def index_view(request):
#     return render(request, 'index.html', context)
# #
#
# def shop_view(request):
#     return render(request, 'shop.html', {})
#
# #
# def single_product_details_view(request):
#     return render(request, 'single-product-details.html', {})


#
#
# def checkout_view(request):
#     return render(request, 'checkout.html', context)
#
#
def regular_page_view(request):
    return render(request, 'regular-page.html', {})
#
#
# def contact_view(request):
#     return render(request, 'contact.html', context)
