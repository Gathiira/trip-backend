from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

loading_list = views.LoadingViewSet.as_view({
    'get':'list',
    'post':'create',
})

loading_detail = views.LoadingViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy',
})

trip_list = views.TripViewSet.as_view({
    'get':'list',
    'post':'create',
})

trip_detail = views.TripViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy',
})

offloading_list = views.OffloadingViewSet.as_view({
    'get':'list',
    'post':'create',
})

offloading_detail = views.OffloadingViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy',
})

trip_info_list = views.TripInfoViewSet.as_view({
    'get':'list',
    'post':'create',
})

trip_info_detail = views.TripInfoViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy',
})


urlpatterns = [
	path('trip/', trip_list,name='trip_list'),
	path('trip/<int:id>/', trip_detail,name='trip_details'),
	path('trip/<int:id>/loading/', loading_list, name = 'loading-detail'),
    path('trip/<int:id>/loading/<int:pk>/', loading_detail, name='loading-details'),
	path('offloading/', offloading_list, name = 'offloading-detail'),
    path('offloading/<int:id>/', offloading_detail, name='offloading-details'),
	path('trip_info/', trip_info_list, name = 'trip_info-detail'),
    path('trip_info/<int:id>/', trip_info_detail, name='trip_info-details'),
]

