# Description: Category API views.

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from ..models import Category
from .serializers import CategorySerializer
from apps.lib.permissions import IsAdminOrReadOnly

class CategoryListAPIView(generics.ListAPIView):
    """
    API view to retrieve the list of all active categories.
    Accessible by any user (no authentication required).
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve the list of all categories or create a new category.
    - GET: accessible only by admin users.
    - POST: accessible only by admin users.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a category instance.
    - GET: accessible by any user (read-only).
    - PUT/PATCH/DELETE: restricted to admin users only.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]