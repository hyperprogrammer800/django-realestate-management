from django.shortcuts import render
from .models import Property, Unit
from django.contrib.auth.decorators import login_required
from .forms import PropertySearchForm, UnitSearchForm

@login_required
def property(request):
    if request.method == 'POST':
        p_form = PropertySearchForm(request.POST)
        un_form = UnitSearchForm(request.POST)
        if p_form.is_valid() and un_form.is_valid():
            prop_data = p_form.cleaned_data
            unit_data = un_form.cleaned_data
            properties = Property.objects.filter(**prop_data)
            units = Unit.objects.filter(**unit_data)
    else:
        units = Unit.objects.all()
        properties = Property.objects.all()
        p_form = PropertySearchForm()
        un_form = UnitSearchForm()
    context = {
        'units' : units,
        'properties' : properties,
        'p_form' : p_form,
        'un_form' : un_form,
    }
    return render(request, 'management/home.html', context)

def tenant(request):
    return render(request, 'management/tenant_home.html',{'title' : 'tenant'})