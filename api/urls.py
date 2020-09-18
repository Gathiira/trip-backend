from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

trip_loading_list = views.TripLoadingViewSet.as_view({
    'get':'list',
    'post':'create',
})

trip_loading_detail = views.TripLoadingViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy',
})

trip_offloading_list = views.TripOffloadingViewSet.as_view({
    'get':'list',
    'post':'create',
})

trip_offloading_detail = views.TripOffloadingViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy',
})

urlpatterns = [
	path('loading/', trip_loading_list,name='loading_list'),
	path('loading/<int:id>/', trip_loading_detail,name='loading_details'),
	path('offloading/', trip_offloading_list, name = 'offloading-detail'),
    path('offloading/<int:id>/', trip_offloading_detail, name='offloading-details'),
]

