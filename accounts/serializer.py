from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

from .models import User, UserProfile, StaffProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    user_profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'user_profile']

        lookup_field = 'id'

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'Username should only contain alphanumeric character')
        return attrs

    def create(self, validated_data):
        user_profile = validated_data.pop('user_profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **user_profile)
        return user


class StaffProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfile
        fields = ['first_name', 'last_name']


class StaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    staff_profile = StaffProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'staff_profile']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'Username should only contain alphanumeric character')
        return attrs

    def create(self, validated_data):
        staff_profile = validated_data.pop('staff_profile')
        user = User.objects.create_staff(**validated_data)
        StaffProfile.objects.create(user=user, **staff_profile)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'is_staff', 'tokens']

        extra_kwargs = {
            'is_staff': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if not user.is_active:
                raise AuthenticationFailed(
                    'ACCOUNT DEACTIVATED, contact admin')
            if not user.is_verified:
                raise AuthenticationFailed('Activate your email to login')
            return {
                'email': user.email,
                'is_staff': user.is_staff,
                'tokens': user.tokens,
            }
        raise AuthenticationFailed("User not found, please REGISTER")


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=68, min_length=5)

    class Meta:
        fields = 'email'
