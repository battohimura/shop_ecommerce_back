from rest_framework import serializers

from .models import Product

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'details', 'price', 'gender', 'stock', 'deleted']