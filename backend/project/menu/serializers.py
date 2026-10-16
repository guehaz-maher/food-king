from rest_framework import serializers
from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source = 'category.name')
    class Meta:
        model = MenuItem
        fields = '__all__'