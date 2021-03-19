import json
from django.conf import settings
from rest_framework import permissions
import jwt

from accounts import models as account_models


def decode_jwt(jwt_code):
    response = jwt.decode(jwt_code, settings.SECRET_KEY)
    return response


def get_authentication_status(auth_headers):
    payload = decode_jwt(auth_headers)
    try:
        user = account_models.User.objects.get(id=payload['user_id'])
        if user.is_verified:
            return user.is_staff
        else:
            return False

    except jwt.ExpiredSignatureError as e:
        print(e)
        return False
    except jwt.DecodeError as e:
        print(e)
        return False


def check_role_status(request, role_name, roles):
    if not request.headers.get('Authorization'):
        return False

    auth_headers = {
        'Authorization': request.headers.get('Authorization')
    }
    try:
        acl_object = get_authentication_status(auth_headers)
    except Exception:
        return False
    if acl_object:
        if role_name in roles:
            return True
        else:
            return False
    else:
        return False


def role_required(role_name, auth_headers):
    class RoleRequired(permissions.BasePermission):
        def has_permission(self, request, view):
            auth_status = check_role_status(request, role_name)
            if auth_status:
                return True
            else:
                return False
    return RoleRequired


def is_authenticated(auth_headers):
    class IsAuthenticated(permissions.BasePermission):
        def has_permission(self, request, view):
            auth_status = get_authentication_status(auth_headers)
            if auth_status:
                return True
            else:
                return False
    return IsAuthenticated
