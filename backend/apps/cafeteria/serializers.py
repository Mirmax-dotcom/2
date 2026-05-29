from rest_framework import serializers
from .models import MenuItem, Shift, Order, OrderItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'description', 'category', 'price', 'composition', 
                  'calories', 'proteins', 'fats', 'carbohydrates', 'allergens', 
                  'is_available', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ('id', 'name', 'start_time', 'end_time', 'created_at')
        read_only_fields = ('id', 'created_at')

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(),
        write_only=True,
        source='menu_item'
    )
    
    class Meta:
        model = OrderItem
        fields = ('id', 'menu_item', 'menu_item_id', 'quantity', 'price', 'created_at')
        read_only_fields = ('id', 'price', 'created_at')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user_fullname = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ('id', 'user', 'user_fullname', 'shift', 'total_amount', 'status', 
                  'order_date', 'delivery_date', 'notes', 'items', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'total_amount', 'created_at', 'updated_at')
    
    def get_user_fullname(self, obj):
        return obj.user.get_full_name() or obj.user.username

class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    
    class Meta:
        model = Order
        fields = ('shift', 'order_date', 'delivery_date', 'notes', 'items')
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        total_amount = 0
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            total_amount += item_data['price'] * item_data.get('quantity', 1)
        
        order.total_amount = total_amount
        order.save()
        return order
