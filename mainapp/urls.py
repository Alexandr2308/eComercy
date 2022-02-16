from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    # path('category/<slug:slug>', CategoryListView.as_view(), name='category-view'),
    path('category/shorts', ShortViews.as_view(), name='shorts-view'),
    path('category/jackets', JacketViews.as_view(), name='jackets-view'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('single-product-details/<slug:slug>', ProductDetailView.as_view(), name='single-product-details'),
    path('checkout/', checkout_view, name='checkout'),
    path('about-us/', regular_page_view, name='about-us'),
    path('accounts/', register, name='register'),
    path('auth-user/', aut_user, name='auth-user'),
    # path('contact/', contact_view, name='contact'),
    path('cart/', cart_detail, name='cart_details'),
    path('add/', cart_add, name='cart_add'),
    path('cart_remove/', cart_remove, name='cart_remove'),

]
