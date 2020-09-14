from django.shortcuts import render

from api import models

def viewTrips(request):
    trips = models.TripInfo.objects.all()
    context = {
        'trips':trips
    }
    return render(request,'index.html', context)

