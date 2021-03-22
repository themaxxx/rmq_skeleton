import pika
import json
from settings import *
import handlers_classes


class MessageConsumer(object):

    def __init__(self):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def _handle_message(self, classname, message):
        class_ = getattr(handlers_classes, classname)
        handler = class_(message)

    def _check_message(self, ch, method, properties, body):
        try:
            message = json.loads(body)
            if "message_kind" in message.keys():
                kind = message.get("message_kind")
                if kind in PUBLISHER_KINDS_AND_CLASSES.keys():
                    class_name = PUBLISHER_KINDS_AND_CLASSES.get(kind)
                else:
                    class_name = 'MalformedMessageHandler'
            else:
                class_name = 'MalformedMessageHandler'

            self._handle_message(class_name, message)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as ex:
            print("Eccezione nel check del messaggio")

    def get_messages(self):
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(queue=QUEUE_NAME, on_message_callback=self._check_message)
        self._channel.start_consuming()
