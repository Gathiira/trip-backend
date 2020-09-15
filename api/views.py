from rest_framework.viewsets import ModelViewSet

from .serializers import (
						UserSerializer
						,TripInfoSerializer
						,LoadingSerializer
						,OffloadingSerializer
						,TripSerializer
					)

from .models import Trip,Loading,Offloading,TripInfo


# Create your views here.
class LoadingViewSet(ModelViewSet):
	serializer_class = LoadingSerializer
	queryset = Loading.objects.all()
	lookup_field = 'id'

class TripViewSet(ModelViewSet):
	serializer_class = TripSerializer
	queryset = Trip.objects.all()
	lookup_field = 'id'

class OffloadingViewSet(ModelViewSet):
	serializer_class = OffloadingSerializer
	queryset = Offloading.objects.all()
	lookup_field = 'id'

class TripInfoViewSet(ModelViewSet):
	serializer_class = TripInfoSerializer
	queryset = TripInfo.objects.all()
	lookup_field = 'id'
