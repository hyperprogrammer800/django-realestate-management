from django.urls import path
from . import views

urlpatterns = [
    path('', views.property, name='property-home'),
    path('tenant/', views.tenant, name='tenant-home'),
    
]
