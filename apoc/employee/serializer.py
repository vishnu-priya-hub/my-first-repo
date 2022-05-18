from rest_framework import serializers
from .models import Customer, ComputationResource, ComputationResourceType


class ComputationResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputationResourceType
        fields = '__all__'


class ComputationResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputationResource
        fields = '__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
