from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import CurrentUserSerializer
from rest_framework import viewsets

# Create your views here.

class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer