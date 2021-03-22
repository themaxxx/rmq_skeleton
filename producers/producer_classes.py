from abstract_classes import AbstractMessageProducer


class AMessageProducer(AbstractMessageProducer):

    def _set_producer_kind(self):
        self._producer_kind = "A"


class BMessageProducer(AbstractMessageProducer):

    def _set_producer_kind(self):
        self._producer_kind = "B"


class CMessageProducer(AbstractMessageProducer):

    def _set_producer_kind(self):
        self._producer_kind = "C"


class MalformedMessageProducer(AbstractMessageProducer):

    def _set_producer_kind(self):
        self._producer_kind = "MALFORMED"
