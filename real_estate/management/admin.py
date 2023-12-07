from django.contrib import admin
from .models import Property, Unit, RentalInfo

# Register your models here.

admin.site.register([Property, Unit, RentalInfo])