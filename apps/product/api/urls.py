"""
URL configuration for product app.
"""
from . import product
from django.urls import path

urlpatterns = [
    path('products/', product.ProductListAPIView.as_view(), name='product-list'),
]
