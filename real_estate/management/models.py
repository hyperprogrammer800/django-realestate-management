from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

def default_end_date():
    return timezone.now() + timedelta(days=365)

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    CHOICES = (
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    )
    type = models.CharField(max_length=4, choices=CHOICES)

    def __str__(self):
        return f"{self.property.name} - {self.type}"


# class Tenant(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=50, null=True)
#     documents =  models.FileField(upload_to='document_files', null=True)

#     def __str__(self):
#         return self.username


class RentalInfo(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE, related_name='rental_info')
    end_date = models.DateField(default=default_end_date)
    rent_date = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tenant.username} rented {self.unit.type} in {self.unit.property.name}"
