from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from django.contrib.auth.models import User

from .serializer import UserSerializer,RegisterSerializer, LoginSerializer

# Create your views here.

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        _,token = AuthToken.objects.create(user)
        return Response({
            'user':UserSerializer(user,context=self.get_serializer()).data,
            'token':token
        })

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        _,token = AuthToken.objects.create(user)
        return Response({
            'user':UserSerializer(user,context=self.get_serializer()).data,
            'token':token
        })

class UserAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
