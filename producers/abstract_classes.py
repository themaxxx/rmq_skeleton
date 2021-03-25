import pika
import json
from abc import ABC, abstractmethod
from settings import *


class AbstractMessageProducer(ABC):
    """
        Abstract class producer.
        Implements connection handling, channel configuration, queue declaration, producer kind handling
    """
    def __init__(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=QUEUE_NAME, durable=True)
        self._set_producer_kind()

    @abstractmethod
    def _set_producer_kind(self):
        self._producer_kind = None
        print("You must implement this method in a subclass!")

    def publish_message(self):
        message_value = "message from producer of kind : {kind}".format(kind=self._producer_kind)
        message = {
            "message_kind": self._producer_kind,
            "message_value": message_value,
        }
        json_message = json.dumps(message)
        self._channel.basic_publish(
            routing_key=QUEUE_NAME,
            exchange=EXCHANGE,
            body=json_message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )
        print(message_value)
