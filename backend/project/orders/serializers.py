from rest_framework import serializers
from .models import Order, OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    items = OrderSerializer(many = True, read_only = True)
    class Meta:
        model = OrderItem
        fields = '__all__'