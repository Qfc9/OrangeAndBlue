import socket
import sys
import threading
import pickle

class UDPListener(threading.Thread):
    """docstring for UDPListener."""

    def __init__(self):
        super(UDPListener, self).__init__()

    def run(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind the socket to the port
        server_address = ('192.168.0.138', 10000)
        print('starting up on %s port %s' % server_address, file=sys.stderr)
        sock.bind(server_address)
        while True:
            print('\nwaiting to receive message', file=sys.stderr)
            data, address = sock.recvfrom(4096)
            data_arr = pickle.loads(data)

            print('received %s bytes from %s' % (len(data), address), file=sys.stderr)
            print(data_arr, file=sys.stderr)
