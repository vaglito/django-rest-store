"""
URL configuration for product app.
"""
from . import product
from django.urls import path

urlpatterns = [
    path('products/', product.ProductList.as_view(), name='product-list'),
]
