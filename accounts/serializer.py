from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['username','is_staff']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['username','email','password','contribution','phone']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        user = Member.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid username or password')
