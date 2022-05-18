from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import generics, mixins
from .serializer import CustomerSerializer, ComputationResourceSerializer, ComputationResourceTypeSerializer
from .models import Customer, ComputationResource, ComputationResourceType
from datetime import datetime
from producer import producer
from django.conf import settings
import json
from pymongo import MongoClient


class CustomerCreateApi(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request,*args, **kwargs ):

        now = datetime.now()
        x = {
            "operation": "Create",
            # "user": Customer.name,
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "Customer"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)

        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)


        return self.create(request, *args, **kwargs)



class CustomerApi(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomerUpdateApi(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):

        now = datetime.now()
        x = {
            "operation": "Update",
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "Customer"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.update(request,*args, **kwargs)


class CustomerDeleteApi(generics.GenericAPIView,mixins.DestroyModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def delete(self, request, *args, **kwargs):

        now = datetime.now()
        x = {
            "operation": "Delete",
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "Customer"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.destroy(request,*args, **kwargs)




class ComputationResourceTypeCreateApi(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer

    def post(self, request, *args, **kwargs):
        now = datetime.now()
        x = {
            "operation": "Create",
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "ComputationResourceType"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.create(request, *args, **kwargs)


class ComputationResourceTypeApi(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ComputationResourceTypeUpdateApi(generics.UpdateAPIView):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        x = {
            "operation": "Update",
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "ComputationResourceType"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.update(request, *args, **kwargs)


class ComputationResourceTypeDeleteApi(generics.GenericAPIView,mixins.DestroyModelMixin):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer
    def delete(self, request, *args, **kwargs):

        now = datetime.now()
        x = {
            "operation": "Delete",
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "ComputationResourceType"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.destroy(request, *args, **kwargs)


class ComputationResourceCreateApi(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer

    def post(self, request, *args, **kwargs):
        now = datetime.now()
        x = {
            "operation": "Create",
            # "user": Customer.name,
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "ComputationResource"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.create(request, *args, **kwargs)


class ComputationResourceApi(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ComputationResourceUpdateApi(generics.UpdateAPIView):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        x = {
            "operation": "Update",
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "ComputationResource"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.update(request, *args, **kwargs)

class ComputationResourceDeleteApi(generics.GenericAPIView,mixins.DestroyModelMixin):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer
    def delete(self, request, *args, **kwargs):

        now = datetime.now()
        x = {
            "operation": "Delete",
            "timestamp": now.strftime("%m/%d/%Y, %H:%M:%S"),
            "status": "success",
            "entity": "ComputationResource"
        }
        msg = x
        pro = producer.kafka_producer(settings.KAFKA_TOPIC)
        pro.send_message(msg)
        myclient = MongoClient("mongodb://localhost:27017/")
        db = myclient["kafka_logs"]
        Collection = db["all_logs"]
        if isinstance(x, list):
            Collection.insert_many(x)
        else:
            Collection.insert_one(x)

        return self.destroy(request, *args, **kwargs)






