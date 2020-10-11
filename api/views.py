from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import (
						TripLoadingSerializer
						,TripOffloadingSerializer
						,UserProfitShareSerializer
						,ProfitShareSerializer
					)
from .models import TripLoading,TripOffloading,SharesModel

class TripLoadingViewSet(ModelViewSet):
	serializer_class = TripLoadingSerializer
	queryset = TripLoading.objects.all()
	ordered_queryset = queryset.order_by('departure_date')
	lookup_field = 'id'
	ordering_fields = ['departure_date', '-id']

class TripOffloadingViewSet(ModelViewSet):
	serializer_class = TripOffloadingSerializer
	queryset = TripOffloading.objects.all()
	lookup_field = 'id'

class UserProfitShareViewSet(ModelViewSet):
	serializer_class = UserProfitShareSerializer
	queryset = SharesModel.objects.all().select_related('user')
	lookup_field = 'id'

class ProfitShareViewSet(ModelViewSet):
	serializer_class = ProfitShareSerializer
	queryset = SharesModel.objects.all().select_related('offloading')
	lookup_field = 'id'