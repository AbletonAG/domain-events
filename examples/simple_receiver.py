#!/usr/bin/env python

import sys

from domain_events import Receiver, DEFAULT_CONNECTION_SETTINGS


def log_event(event):
    print " [x] {}".format(event)


if __name__ == '__main__':
    binding_keys = sys.argv[1:]
    receiver = Receiver(DEFAULT_CONNECTION_SETTINGS)
    receiver.register(log_event, name='simple-receiver', binding_keys=binding_keys)
    receiver.start_consuming()
