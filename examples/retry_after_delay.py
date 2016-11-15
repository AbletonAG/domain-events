#!/usr/bin/env python

import logging
import sys

from domain_events import Receiver, Retry, DEFAULT_CONNECTION_SETTINGS


logging.basicConfig(level=logging.INFO)


def handler(event):
    delay = 5.0 + (10.0 * event.retries)
    raise Retry(delay)


if __name__ == '__main__':
    binding_keys = sys.argv[1:]
    receiver = Receiver(DEFAULT_CONNECTION_SETTINGS)
    receiver.register(handler, name='retry-ronny', binding_keys=binding_keys, max_retries=3)
    receiver.start_consuming()
