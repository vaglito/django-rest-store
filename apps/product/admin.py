from django.contrib import admin
from .models import Product, Category

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'price', 'catetegory', 'created_at']
    search_fields = ['name', 'pk']
    list_filter = ['catetegory', 'created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'pk']