from abstract_classes import AbstractMessageHandler


class A_MessageHandler(AbstractMessageHandler):

    def _handle_message(self):
        print(self._message_value)


class B_MessageHandler(AbstractMessageHandler):

    def _handle_message(self):
        print(self._message_value)


class C_MessageHandler(AbstractMessageHandler):

    def _handle_message(self):
        print(self._message_value)


class MalformedMessageHandler(AbstractMessageHandler):

    def _handle_message(self):
        print("MESSAGGIO MALFORMATO")
        print(self._message_kind)
        print(self._message_value)
