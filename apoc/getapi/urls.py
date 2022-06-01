from django.urls import path
from .views import getAllApi, get_by_customer, get_by_resource, get_by_computation_resource_type


urlpatterns = [
    path('getall', getAllApi),
    path('customer', get_by_customer),
    path('resource', get_by_resource),
    path('resourcetype', get_by_computation_resource_type)
]
