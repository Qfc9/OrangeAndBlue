import socket
import sys
import os, platform, subprocess, re
import multiprocessing
from psutil import virtual_memory
import tensorflow as tf
from tensorflow.python.client import device_lib
import imAlive


def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    thread1 = imAlive.ImAlive()
    thread1.start()

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address, file=sys.stderr)
    sock.connect(server_address)

    try:

        # Send data
        message = 'This is the message.  It will be repeated.'
        print('sending "%s"' % message, file=sys.stderr)
        sock.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data, file=sys.stderr)

    finally:
        print('closing socket', file=sys.stderr)
        sock.close()


if __name__ == '__main__':
    main()
