from django.shortcuts import render
from .models import Property, Unit, RentalInfo
from django.contrib.auth.models import User

# Create your views here.
# 2.2.Property Listing Module 

# PropertyDetails:Create propertyprofilewithinformationlike Property name 
# and address, location, features. 
# Eachproperty will have multiple units.Each unit will have features like 
# rent cost,Type- 1BHK,2BHK,3BHK,4BHK 
# propertyprofile view with units and assigned tenant information

properties = [
    {
        'name' : 'Alaphane Medows',
        'address' : '18, Thiruneermalai Main Road, Chromepet',
        'location' : 'Chennai',
        'units' : [
            {
                'rent' : 10000,
                'type' : '1BHK'
            },
            {
                'rent' : 15000,
                'type' : '2BHK'
            }
        ]
    },
    {
        'name' : 'Casa Grande',
        'address' : '6, East Street, Tambaram',
        'location' : 'Chennai',
        'units' : [
            {
                'rent' : 20000,
                'type' : '3BHK'
            },
            {
                'rent' : 25000,
                'type' : '4BHK'
            }
        ]
    }
]


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