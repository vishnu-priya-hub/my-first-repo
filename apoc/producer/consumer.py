import ast
import json
import pdb
from json import encoder
from django.http import JsonResponse
import threading
from kafka import KafkaConsumer
from django.conf import settings

class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):

        consumer = KafkaConsumer(
            settings.KAFKA_TOPIC,
            bootstrap_servers=settings.KAFKA_HOST + ':' + settings.KAFKA_PORT,
            auto_offset_reset='earliest',
            group_id='group1',
            value_deserializer= lambda x: json.dumps(x.decode('utf-8'))
        )

        messages = []
        for message in consumer:
            message = message.value
            messages.append(message)
            print('{}'.format(message))
            #print(message)
        return messages
