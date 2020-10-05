from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import (
						TripLoadingSerializer
						,TripOffloadingSerializer
						,UserProfitShareSerializer
					)
from .models import TripLoading,TripOffloading,SharesModel

class TripLoadingViewSet(ModelViewSet):
	serializer_class = TripLoadingSerializer
	queryset = TripLoading.objects.all()
	lookup_field = 'id'
	ordering ='departure_date'

class TripOffloadingViewSet(ModelViewSet):
	serializer_class = TripOffloadingSerializer
	queryset = TripOffloading.objects.all()
	lookup_field = 'id'

class UserProfitShareViewSet(ModelViewSet):
	serializer_class = UserProfitShareSerializer
	queryset = SharesModel.objects.all()
	lookup_field = 'id'