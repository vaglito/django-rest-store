import django_filters as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__slug', lookup_expr='icontains')
    price = filters.RangeFilter()
    created_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'created_at']