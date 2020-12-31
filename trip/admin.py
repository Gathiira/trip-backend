from django.contrib import admin

from .models import (
    TripRequest, TripLoading,
    TripOffloading, TripExpense, TripShare)

admin.site.register(TripRequest)
admin.site.register(TripLoading)
admin.site.register(TripOffloading)
admin.site.register(TripExpense)
admin.site.register(TripShare)