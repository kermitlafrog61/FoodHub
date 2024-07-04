from django.db.models.manager import BaseManager
from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        iterable = data.all() if isinstance(data, BaseManager) else data

        return [
            {
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'photo': item.photo.url if item.photo else None,
            }
            for item in iterable
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'ingredients', 'price', 'photo', 'novelty',)
        list_serializer_class = ProductListSerializer
