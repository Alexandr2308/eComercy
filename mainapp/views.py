from urllib import request

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *
from .cart import Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', {'cart': cart})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'register_user.html', {'form': form})


def auth_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            auth_form = UserAuthForm(request.POST)
            return render(request, 'aut-user.html', {'auth_form': auth_form})
    else:
        auth_form = UserAuthForm()
        return render(request, 'aut-user.html', {'auth_form': auth_form})


def logout_view(request):
    logout(request)
    return redirect('home')


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
    add_product_form = super(CartAddProductForm)





#
    def post(self, request, *args, **kwargs):
        self.add_product_form = CartAddProductForm()
        print('hello')
        # product = Product.objects.get()
        # context = {'price': product.price,
        #            'image': product.image,
        #            'id': product.id,
        #            'title': product.title,
        #            'description': product.description,
        #            'add_product_form': add_product_form}
        if request.method == 'POST':
            cart = Cart(request)
            form = CartAddProductForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                cart.add(
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
                return redirect('cart_add')
            else:
                return redirect('shop')
        return super(ProductDetailView, self).get(request, *args, **kwargs)





# def product_detail_view(request, slug):
#     add_product_form = CartAddProductForm()
#     product = Product.objects.get(slug=slug)
#     context = {'price': product.price,
#                'image': product.image,
#                'id': product.id,
#                'title': product.title,
#                'description': product.description,
#                'add_product_form': add_product_form}
#     if request.method == 'POST':
#         cart = Cart(request)
#         form = CartAddProductForm(request.POST)
#         print(form)
#         print(cart)
#         if form.is_valid():
#             cd = form.cleaned_data
#             cart.add(product=product,
#                      quantity=cd['quantity'],
#                      update_quantity=cd['update'])
#             print(cart)
#             return redirect('cart_add')
#         else:
#             return redirect('auth-user')
#     return render(request, 'single-product-details.html', context)



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
