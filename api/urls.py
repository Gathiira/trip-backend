from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False) #
router.register(r'loading', views.TripLoadingViewSet, 'loading')
router.register(r'offloading', views.TripOffloadingViewSet, 'offloading')
router.register(r'shares', views.UserProfitShareViewSet, 'shares')

urlpatterns = router.urls

