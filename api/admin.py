from django.contrib import admin

# Register your models here.

from .models import TripLoading, TripOffloading, SharesModel,UserContribution

admin.site.register(TripLoading)
admin.site.register(TripOffloading)
admin.site.register(SharesModel)
admin.site.register(UserContribution)