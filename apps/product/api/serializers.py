# Description: Serializers for the product app.

from apps.product.models import Product, Category
from rest_framework import serializers


# Create serializers here
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='catetegory', write_only=True
    )
    catetegory = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category_id', 'catetegory', 'price', 'slug', 'created_at', 'updated_at']