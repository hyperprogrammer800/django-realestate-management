from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Property, Unit

class PropertySearchForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location']

class UnitSearchForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['rent_cost', 'type']