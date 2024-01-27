from rest_framework import serializers
from .models import Purchase, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['shortDescription', 'price']

class PurchaseSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ['uuid', 'retailer', 'purchaseDate', 'purchaseTime', 'total', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        purchase = Purchase.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(purchase=purchase, **item_data)
        return purchase
