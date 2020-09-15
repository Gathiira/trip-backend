from django.contrib import admin

# Register your models here.

from .models import Trip,TripInfo, Loading,Offloading

admin.site.register(Trip)
admin.site.register(TripInfo)
admin.site.register(Loading)
admin.site.register(Offloading)