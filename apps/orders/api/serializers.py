from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.product.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.

    - Displays the ID, product reference, quantity, and calculated price of each item.
    - Includes a read-only field to show the product's name for display purposes.
    """
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_name',
            'quantity',
            'price'
        ]


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    - Handles nested representation of related OrderItems.
    - Automatically assigns the logged-in user's username (read-only).
    - Calculates and saves the total price of the order during creation.
    """
    items = OrderItemSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'status',
            'total_price',
            'created_at',
            'items'
        ]
        read_only_fields = ['user']

    def create(self, validated_data):
        """
        Custom create method to handle nested OrderItem creation.

        - Extracts and processes item data from the validated input.
        - Calculates the total price of the order based on product prices and quantities.
        - Creates the Order and associated OrderItems in the database.
        """
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total = 0

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price * quantity
            total += price

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price
            )

        order.total_price = total
        order.save()
        return order
