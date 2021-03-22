from abstract_classes import AbstractMessageProducer


class AMessageProducer(AbstractMessageProducer):
    """
        Producer class for kind A messages
    """
    def _set_producer_kind(self):
        self._producer_kind = "A"


class BMessageProducer(AbstractMessageProducer):
    """
        Producer class for kind B messages
    """
    def _set_producer_kind(self):
        self._producer_kind = "B"


class CMessageProducer(AbstractMessageProducer):
    """
        Producer class for kind C messages
    """
    def _set_producer_kind(self):
        self._producer_kind = "C"


class MalformedMessageProducer(AbstractMessageProducer):
    """
        Producer class for kind MALFORMED messages
    """
    def _set_producer_kind(self):
        self._producer_kind = "MALFORMED"
