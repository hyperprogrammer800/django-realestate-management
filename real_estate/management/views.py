from django.shortcuts import render
from .models import Property, Unit


def property(request):
    units = Unit.objects.all()
    properties = Property.objects.all()
    context = {
        'units' : units,
        'properties' : properties
    }
    return render(request, 'management/home.html', context)

def tenant(request):
    return render(request, 'management/tenant_home.html',{'title' : 'tenant'})