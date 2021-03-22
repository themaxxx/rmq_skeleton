from abc import abstractmethod


class AbstractMessageHandler(object):
    """
        Abstract class Message Handler.
        Handles received messages by kind.
    """
    def __init__(self, message):
        self._message = message
        self._message_kind = None
        self._message_value = None
        self._load_message()
        self._handle_message()

    def _load_message(self):
        try:
            self._message_kind = self._message.get("message_kind")
            self._message_value = self._message.get("message_value")
        except Exception as ex:
            print("Eccezione nell'handler")

    @abstractmethod
    def _handle_message(self):
        raise Exception("You MUST implement this method in a subclass")
