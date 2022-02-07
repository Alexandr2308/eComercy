import self
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import UserAuthForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'register_user.html', {'form': form})


def aut_user(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserAuthForm()
    return render(request, 'aut-user.html', {'form': form})


class IndexView(ListView):
    model = Product
    template_name = 'index.html'


class ShopView(ListView):
    model = Product
    paginate_by = 1
    template_name = 'shop.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'single-product-details.html'


#
# class CategoryListView(ListView):
#     model = Product
#     template_name = 'category.html'

class ShortViews(ListView):
    model = Shorts
    paginate_by = 1
    template_name = 'shorts.html'


class JacketViews(ListView):
    model = Jacket
    paginate_by = 1
    template_name = 'jackets.html'


def checkout_view(request):
    return render(request, 'checkout.html', {})


def regular_page_view(request):
    return render(request, 'regular-page.html', {})

# def contact_view(request):
#     return render(request, 'contact.html', context)
