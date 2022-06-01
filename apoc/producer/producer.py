from logging import Logger
from kafka import KafkaProducer
from json import dumps
import logging
from django.conf import settings

# from apoc.apoc.settings import KAFKA_HOST, KAFKA_PORT, KAFKA_RETRIES
log: Logger = logging.getLogger(__name__)


class KafkaConnector(object):
    def __init__(self):
        self.server = settings.KAFKA_HOST + ":" + str(settings.KAFKA_PORT)
        self.retries = settings.KAFKA_RETRIES

    # creates new kafka connection
    def create_connection(self):
        producer = KafkaProducer(bootstrap_servers=self.server, retries=self.retries,
                                 value_serializer=lambda x: dumps(x).encode('utf-8'))
        return producer

    # For explicitly opening database connection
    def __enter__(self):
        self.kafkaconn = self.create_connection()
        return self.kafkaconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.kafkaconn.close()


class kafka_producer(object):
    connection = None

    def __init__(cls, topic):
        cls.topic = topic

    def get_topic(cls):
        return cls.topic

    @classmethod
    def get_kafka_connection(cls, new: object = False) -> object:
        """Creates return new Singleton kafka connection"""
        if new or not cls.connection:
            cls.connection = KafkaConnector().create_connection()
            return cls.connection

    def send_message(cls, msg):
        connection = cls.get_kafka_connection()

        try:
            if type(msg) is list:
                # log.info("**********Multiple processed message sent**********")
                for item in msg:
                    connection.send(cls.topic, value=item).add_callback(cls.success).add_errback(cls.error)
            else:
                # log.info("**********Single processed message sent**********")
                connection.send(cls.topic, value=msg)
        except Exception as e:
            log.info(e)
            log.info("Error connecting to kafka")
            return

    def success(cls, metadata):
        log.info(metadata.topic)

    def error(cls, exception):
        log.info(exception)
