"""
URL configuration for product app.
"""
from . import product
from . import category
from django.urls import path

urlpatterns = [
    path('products/', product.ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', product.ProductListCreateAPIView.as_view(), name='product-create'),
    path('products/<int:pk>/', product.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('categories/', category.CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', category.CategoryListCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/', category.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
]
