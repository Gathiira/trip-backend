from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'account', UserViewSet, basename='account')

urlpatterns = router.urls