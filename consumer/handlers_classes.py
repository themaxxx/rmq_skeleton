from abstract_classes import AbstractMessageHandler


class A_MessageHandler(AbstractMessageHandler):
    """
        Message handler class for kind A messages
    """
    def _handle_message(self):
        print(self._message_value)


class B_MessageHandler(AbstractMessageHandler):
    """
        Message handler class for kind B messages
    """
    def _handle_message(self):
        print(self._message_value)


class C_MessageHandler(AbstractMessageHandler):
    """
        Message handler class for kind C messages
    """
    def _handle_message(self):
        print(self._message_value)


class MalformedMessageHandler(AbstractMessageHandler):
    """
        Message handler class for kind MALFORMED messages
    """
    def _handle_message(self):
        print("MESSAGGIO MALFORMATO")
        print(self._message_kind)
        print(self._message_value)
