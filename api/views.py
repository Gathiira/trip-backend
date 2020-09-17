from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from .serializers import (
						UserSerializer
						,TripLoadingSerializer
						,TripOffloadingSerializer
					)
from .models import TripLoading,TripOffloading


# Create your views here.
class UserViewSet(ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	lookup_field = 'id'

class TripLoadingViewSet(ModelViewSet):
	serializer_class = TripLoadingSerializer
	queryset = TripLoading.objects.all()
	lookup_field = 'id'

class TripOffloadingViewSet(ModelViewSet):
	serializer_class = TripOffloadingSerializer
	queryset = TripOffloading.objects.all()
	lookup_field = 'id'