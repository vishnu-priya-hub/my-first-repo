import json
from bson import json_util
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
import pymongo
from rest_framework.response import Response



@api_view(['GET'])
def getAllApi(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["kafka_logs"]
    collection = db["all_logs"]
    msg = collection.find()
    message = []
    if msg:
        for data in msg:
            message.append(data)
        return Response(json.loads(json_util.dumps(message)))
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_by_computation_resource_type(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["kafka_logs"]
    collection = db["all_logs"]
    msg = collection.find({"entity": "ComputationResourceType"})
    message = []
    if msg:
        for data in msg:
            message.append(data)
        return Response(json.loads(json_util.dumps(message)))
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_by_resource(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["kafka_logs"]
    collection = db["all_logs"]
    msg = collection.find({"entity": "ComputationResource"})

    message = []
    if msg:
        for data in msg:
            message.append(data)
        return Response(json.loads(json_util.dumps(message)))
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_by_customer(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["kafka_logs"]
    collection = db["all_logs"]
    msg = collection.find({"entity": "Customer"})
    message = []
    if msg:
        for data in msg:
            message.append(data)
        return Response(json.loads(json_util.dumps(message)))
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

