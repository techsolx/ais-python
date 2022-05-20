#! /bin/env python3

from pyais.stream import UDPReceiver

host = "127.0.0.1"
port = 10110

for msg in UDPReceiver(host, port):
    print(msg.decode())
