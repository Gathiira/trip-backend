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

shares_list = views.UserProfitShareViewSet.as_view({
    'get':'list',
    'post':'create',
})

shares_detail = views.UserProfitShareViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy',
})


view_shares_list = views.ProfitShareViewSet.as_view({
    'get':'list'
})

urlpatterns = [
	path('loading/', trip_loading_list,name='loading_list'),
	path('loading/<int:id>/', trip_loading_detail,name='loading_details'),
	path('offloading/', trip_offloading_list, name = 'offloading-detail'),
    path('offloading/<int:id>/', trip_offloading_detail, name='offloading-details'),
	path('shares/', shares_list, name = 'shares-detail'),
	path('view-shares/', view_shares_list, name = 'view-shares-detail'),
    path('shares/<int:id>/', shares_detail, name='shares-details'),
]

