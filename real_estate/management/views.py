from django.shortcuts import render
from .models import Property, Unit, RentalInfo
from django.contrib.auth.models import User


def property(request):
    units = Unit.objects.all()
    rents = RentalInfo.objects.all()
    properties = Property.objects.all()
    context = {
        'rents' : rents,
        'units' : units,
        'properties' : properties
    }
    return render(request, 'management/home.html', context)

def tenant(request):
    return render(request, 'management/tenant_home.html',{'title' : 'tenant'})