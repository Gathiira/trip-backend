from django.conf import settings
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import (
                                smart_str, 
                                force_str, 
                                smart_bytes, 
                                DjangoUnicodeDecodeError)
from django.utils.http import (
                            urlsafe_base64_encode, 
                            urlsafe_base64_decode)
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken

import jwt

from .serializer import (
    UserSerializer, 
    LoginSerializer,
    StaffSerializer, 
    PasswordResetSerializer
)
from .models import User
from shared_functions import (renderers,notifications) 

notification = notifications
renderer = renderers

class UserViewSet(viewsets.ModelViewSet):

    renderer_classes = (renderer.UserRenderer,)

    @action(
        methods=['POST'], 
        detail=False, 
        url_path='login', 
        url_name='login')
    def login_user(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=['POST'], detail=False,
        url_path="register-user", 
        url_name="register_user")
    def register_user(self, request):
        user_data = request.data
        serializer = UserSerializer(data=user_data)
        serializer.is_valid(raise_exception = True) # run validate method
        serializer.save()   # run create method

        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('account-verify_email')

        absolute_url = 'http://' + current_site +\
            relative_link + '?token='+ str(token)

        email_body = 'Hi ' + user.username + \
            "\nClick on the link below to verify your email\n\n"\
                + absolute_url

        payload = {
            'email_body':email_body, 
            'to_email':user.email, 
            'email_subject':"verify your email"
        }

        notification.send_email(payload)

        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED)

    @action(
        methods=['POST'], 
        detail=False, 
        url_path="register-staff", 
        url_name="register_staff")
    def register_staff(self, request):
        user_data = request.data
        serializer = StaffSerializer(data=user_data)
        serializer.is_valid(raise_exception = True) # run validate method
        serializer.save()   # run create method

        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('account-verify_email')

        absolute_url = 'http://' + current_site + \
            relative_link + '?token='+ str(token)
        email_body = 'Hi ' + user.username + \
            "\nClick on the link below to verify your email\n\n" + absolute_url
        payload = {
            'email_body':email_body, 
            'to_email':user.email, 
            'email_subject':"verify your email"
        }

        notification.send_email(payload)

        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED)

    @action(
        methods=['GET'], 
        detail=False, 
        url_path="verify-email", 
        url_name="verify_email")
    def verify_email(self,reguest):
        token = reguest.GET.get('token')
        try:
            payload= jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response(
                {'detail':"Email successfully activated"}, 
                status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            print(e)
            return Response(
                {'error':"Activation link expired!!!"}, 
                status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError as e:
            print(e)
            return Response(
                {'error':"INVALID token"}, 
                status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=['POST'], 
        detail=False, 
        url_path='reset-password', 
        url_name='reset_password')
    def password_reset(self, request):
        serializer = PasswordResetSerializer(data=request.data)

        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request).domain
            relative_link = reverse(
                'account-confirm_password_reset', 
                args={'uidb64': uidb64, 'token': token})

            absolute_url = 'http://' + current_site + relative_link
            email_body = 'Hi\n\n Use the link below to reset your password\n\n' + absolute_url
            payload = {
                'email_body': email_body, 
                'to_email': user.email,
                'email_subject': "Reset Password"}

            notification.send_email(payload)

        return Response(
            {'detail':'A link was sent to your email'}, 
            status=status.HTTP_200_OK)
    
    @action(
        methods=['GET'], 
        detail=False, 
        url_path=r'confirm-password-reset/(?P<uidb64>)/(?P<token>)$', 
        url_name='confirm_password_reset')
    def password_reset_confirm(self, request, uidb64, token):
        pass