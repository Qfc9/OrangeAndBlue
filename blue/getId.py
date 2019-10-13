import socket
import sys
import pickle

def getId():
    id = 0
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address, file=sys.stderr)

    try:
        sock.connect(server_address)
    except Exception as e:
        return id


    try:
        # Send data
        message = dict()
        message["version"] = 1
        message["id"] = id
        message["type"] = 1
        message["length"] = 0

        sock.send(pickle.dumps(message))

        msg = sock.recv(128)
        id = pickle.loads(msg)
        print('received "%s"' % id, file=sys.stderr)
    except Exception as e:
        print(e)

    finally:
        print('closing socket', file=sys.stderr)
        sock.close()

    return id
