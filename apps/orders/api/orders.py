from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Order
from .serializers import OrderSerializer
from apps.utils.permissions import IsAdminOrReadOnly


class OrderListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all orders or create a new order.

    - Authenticated users can list their own orders.
    - Admin users can list all orders.
    - Any authenticated user can create a new order.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return the appropriate queryset based on user role.
        - Admins get all orders.
        - Regular users get only their own orders.
        """
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Automatically assign the logged-in user as the owner of the new order.
        """
        serializer.save(user=self.request.user)


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific order.

    - All users can retrieve their own orders.
    - Admin users can retrieve, update, or delete any order.
    - Only admin users can perform update or delete actions.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        """
        Return the appropriate queryset based on user role.
        - Admins get all orders.
        - Regular users get only their own orders.
        """
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)
