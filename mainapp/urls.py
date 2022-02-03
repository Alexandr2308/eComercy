from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('single-product-details/<slug:slug>', ProductDetailView.as_view(), name='single-product-details'),
    # path('checkout/', checkout_view, name='checkout'),
    path('about-us/', regular_page_view, name='about-us'),
    # path('contact/', contact_view, name='contact'),

]
