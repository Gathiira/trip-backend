import json
from django.conf import settings
from rest_framework import permissions
import jwt

from accounts import models as account_models


def decode_jwt(user_headers):
    try:
        auth_headers = user_headers.get('Authorization')
        jwt_auth = auth_headers.split(' ')[1]
        response = jwt.decode(jwt_auth, settings.SECRET_KEY)
        return response
    except Exception as e:
        print(e)
        return False


def get_authentication_status(auth_headers):
    try:
        payload = decode_jwt(auth_headers)
        user = account_models.User.objects.get(id=payload['user_id'])
        role = None
        if user.is_verified:
            if user.is_staff:
                role = 'STAFF'
            else:
                role = 'PUBLIC'
            return role
        else:
            return False
    except Exception as e:
        print(e)
        return False


def check_role_status(request, role_name, auth_headers):
    try:
        acl_object = get_authentication_status(auth_headers)
    except Exception:
        return False
    if acl_object:
        if role_name == acl_object:
            return True
        else:
            return False
    else:
        return False


def role_required(role_name, auth_headers):
    class RoleRequired(permissions.BasePermission):
        def has_permission(self, request, view):
            auth_status = check_role_status(request, role_name, auth_headers)
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
