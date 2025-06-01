# Description: Product API views.

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer
from ..models import Product
from .serializers import ProductSerializer
from ..filters import ProductFilter
from apps.utils.permissions import IsAdminOrReadOnly

class ProductListAPIView(generics.ListAPIView):
    """
    API view to retrieve the list of all active products.
    Accessible by any user (no authentication required).
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    renderer_classes = [JSONRenderer]

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve the list of all products or create a new product.
    - GET: accessible only by admin users.
    - POST: accessible only by admin users.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a product instance.
    - GET: accessible by any user (read-only).
    - PUT/PATCH/DELETE: restricted to admin users only.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
