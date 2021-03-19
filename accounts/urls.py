from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls
