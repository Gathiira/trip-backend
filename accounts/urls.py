from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profile', views.CurrentUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]