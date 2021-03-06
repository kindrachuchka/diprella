import sys
import logging


class Logging(object):
    __logger = None


    @classmethod
    def getLogger(cls):
        if not Logging.__logger:
            logging.basicConfig(
                                level=logging.DEBUG,
                                format='%(levelname)s:%(message)s'
            )
            logging.getLogger(__name__).addHandler(logging.StreamHandler())
            Logging.__logger = logging
        return Logging.__logger


logger = Logging.getLogger()