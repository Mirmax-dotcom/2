from rest_framework import serializers
from .models import User, PersonalAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'created_at')
        read_only_fields = ('id', 'created_at')

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'role')
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PersonalAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = PersonalAccount
        fields = ('id', 'user', 'account_number', 'balance', 'is_blocked', 'blocked_reason', 'created_at')
        read_only_fields = ('id', 'created_at')

class PersonalAccountDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = PersonalAccount
        fields = ('id', 'user', 'account_number', 'balance', 'is_blocked', 'blocked_reason', 'created_at', 'updated_at')
        read_only_fields = ('id', 'balance', 'created_at', 'updated_at')
