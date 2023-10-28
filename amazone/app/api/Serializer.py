from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import *
from app.models import STATE_CHOICES

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class CustomerSerializer(serializers.ModelSerializer):
    state = serializers.ChoiceField(choices=STATE_CHOICES)

    class Meta:
        model = Customer
        fields = '__all__'