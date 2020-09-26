from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from api.serializers import UserContributionSerializer, UserProfitShareSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    contribution = UserContributionSerializer(read_only=True)
    profit_per_user =  UserProfitShareSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username','is_staff','is_superuser','contribution','profit_per_user']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
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
