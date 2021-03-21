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

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken

import jwt

from accounts import models as accounts_models
from accounts import serializers as accounts_serializers
from shared_functions import (
    renderers, notifications, authentication_functions)

notification = notifications.NotificationClass()
renderer = renderers

authentication_function = authentication_functions


class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['reference_number']

    def get_serializer_context(self):
        context = self.get_headers()
        context.update({
            "user": self.get_authenticated_user_id()
        })
        return context

    renderer_classes = (renderer.UserRenderer,)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'get_user_details':
            permission_classes = [
                authentication_function.is_authenticated(self.get_headers()), ]

        if self.action == 'register_user':
            permission_classes = [
                authentication_function.role_required(
                    "STAFF", self.get_headers()), ]

        if self.action == 'register_staff':
            permission_classes = [
                authentication_function.role_required(
                    "STAFF", self.get_headers()), ]

        return [permission() for permission in permission_classes]

    def get_headers(self):
        headers = {
            'Authorization': self.request.headers.get('Authorization')
        }
        return headers

    def get_authenticated_user_id(self):
        user_headers = self.get_headers()
        decoded_jwt = authentication_function.decode_jwt(user_headers)
        if decoded_jwt:
            user = decoded_jwt['user_id']
            return user
        return False

    def get_application_process(self):
        process_name = "Trip Management"
        return process_name

    @action(
        methods=['POST'],
        detail=False,
        url_path='login',
        url_name='login')
    def login_user(self, request):
        serializer = accounts_serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = serializer.validated_data
        user_details = accounts_serializers.UserDetailsSerializer(
            payload, many=False
        ).data
        return Response(user_details, status=status.HTTP_200_OK)

    @action(
        methods=['GET'],
        detail=False,
        url_path='get-authentication-status',
        url_name='get-authentication-status')
    def get_user_details(self, request):
        user_id = self.get_authenticated_user_id()
        user = accounts_models.User.objects.get(id=user_id)
        user_details = accounts_serializers.AuthenticatedUserDetailsSerializer(
            user, many=False
        ).data
        print(user_details)
        return Response(user_details, status=status.HTTP_200_OK)

    @action(
        methods=['POST'], detail=False,
        url_path="register-user",
        url_name="register_user")
    def register_user(self, request):
        user_data = request.data
        serializer = accounts_serializers.UserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)  # run validate method
        serializer.save()   # run create method

        user = accounts_models.User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        try:
            current_site = get_current_site(request).domain
            relative_link = reverse('user-verify_email')

            absolute_url = 'http://' + current_site +\
                relative_link + '?token=' + str(token)

            email_body = 'Hi ' + user.username + \
                "\nClick on the link below to verify your email\n\n"\
                + absolute_url

            payload = {
                'email_body': email_body,
                'to_email': [user.email],
                'email_subject': "SMOKIN ACE EMAIL VERIFICATION"
            }

            notification.broad_cast_system_notification(payload)
        except Exception as e:
            print(e)
            pass

        return Response(
            {"details": 'successfully created an account',
             "token": serializer.data
             },
            status=status.HTTP_201_CREATED)

    @action(
        methods=['POST'],
        detail=False,
        url_path="register-staff",
        url_name="register_staff")
    def register_staff(self, request):
        user_data = request.data
        serializer = accounts_serializers.StaffSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)  # run validate method
        serializer.save()   # run create method

        user = accounts_models.User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('user-verify_email')

        absolute_url = 'http://' + current_site + \
            relative_link + '?token=' + str(token)
        email_body = 'Hi ' + user.username + \
            "\nClick on the link below to verify your email\n\n" + absolute_url
        payload = {
            'email_body': email_body,
            'to_email': [user.email],
            'email_subject': "verify your email"
        }

        notification.broad_cast_system_notification(payload)

        return Response(
            {"token": token},
            status=status.HTTP_201_CREATED)

    @action(
        methods=['GET'],
        detail=False,
        url_path="verify-email",
        url_name="verify_email")
    def verify_email(self, reguest):
        token = reguest.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = accounts_models.User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(
                    {'detail': "Email successfully activated"},
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {'detail': "Email Already Verified"},
                    status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as e:
            print(e)
            return Response(
                {'error': "Activation link expired!!!"},
                status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError as e:
            print(e)
            return Response(
                {'error': "INVALID token"},
                status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=['POST'],
        detail=False,
        url_path='reset-password',
        url_name='reset_password')
    def password_reset(self, request):
        serializer = accounts_serializers.PasswordResetSerializer(
            data=request.data)

        email = request.data['email']
        if accounts_models.User.objects.filter(email=email).exists():
            user = accounts_models.User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request).domain
            relative_link = reverse(
                'user-confirm_password_reset',
                args={'uidb64': uidb64, 'token': token})

            absolute_url = 'http://' + current_site + relative_link
            email_body = 'Hi\n\n Use the link below to reset your password\n\n' + absolute_url
            payload = {
                'email_body': email_body,
                'to_email': user.email,
                'email_subject': "Reset Password"}

            notification.broad_cast_system_notification(payload)

        return Response(
            {'detail': 'A link was sent to your email'},
            status=status.HTTP_200_OK)

    @action(
        methods=['GET'],
        detail=False,
        url_path=r'confirm-password-reset/(?P<uidb64>)/(?P<token>)$',
        url_name='confirm_password_reset')
    def password_reset_confirm(self, request, uidb64, token):
        pass
