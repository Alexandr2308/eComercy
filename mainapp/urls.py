from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('shop/', shop_view, name='shop'),
    path('single-product-details/', single_product_details_view, name='single-product-details'),
    path('checkout/', checkout_view, name='checkout'),
    path('about-us/', regular_page_view, name='about-us'),
    path('contact/', contact_view, name='contact'),
]


