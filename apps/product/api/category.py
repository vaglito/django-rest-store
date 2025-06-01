# Description: Category API views.
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from ..models import Category
from .serializers import CategorySerializer
from apps.utils.permissions import IsAdminOrReadOnly


@extend_schema(
    summary="List all categories",
    description="Returns a list of all available categories. Accessible to anyone."
)
class CategoryListAPIView(generics.ListAPIView):
    """
    API view to retrieve the list of all active categories.
    Accessible by any user (no authentication required).
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


@extend_schema(
    summary="List or create categories",
    description=(
        "Returns a list of all categories or allows an admin user to create a new one. "
        "Only admin users can perform POST requests."
    )
)
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve the list of all categories or create a new category.
    - GET: accessible only by admin users.
    - POST: accessible only by admin users.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


@extend_schema(
    summary="Retrieve, update, or delete a category",
    description=(
        "Allows any user to retrieve category details. "
        "Only admin users can update or delete categories."
    )
)
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a category instance.
    - GET: accessible by any user (read-only).
    - PUT/PATCH/DELETE: restricted to admin users only.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]