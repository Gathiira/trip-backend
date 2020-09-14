from django.contrib import admin

# Register your models here.

from .models import Task, TripInfo,Member

admin.site.register(Task)
admin.site.register(TripInfo)
admin.site.register(Member)