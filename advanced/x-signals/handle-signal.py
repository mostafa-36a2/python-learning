#!/usr/bin/env python
import signal
import sys

counter = 0
def signal_handler(sig, frame):
    global counter
    print(f'You pressed Ctrl+C! {counter}')
    counter += 1
    if counter==10:
        sys.exit(0)
    signal.pause()

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()