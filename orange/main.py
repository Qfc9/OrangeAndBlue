import socket
import sys
import udpListener
import pickle
import traceback

def main():
    id = 100
    print("Loaded Orange")

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    thread1 = udpListener.UDPListener()
    thread1.start()

    # Bind the socket to the port
    server_address = ('192.168.0.138', 10000)
    print('starting up on %s port %s' % server_address, file=sys.stderr)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection', file=sys.stderr)
        connection, client_address = sock.accept()

        try:
            print('connection from', client_address, file=sys.stderr)

            # Receive the data in small chunks and retransmit it
            head = connection.recv(2000)
            head = pickle.loads(head)
            print('received "%s"' % head, file=sys.stderr)

            if head["type"] == 1:
                connection.send(pickle.dumps((id)))
                id += 1
        except Exception as e:
            # print(e)
            traceback.print_exc()
        finally:
            # Clean up the connection
            connection.close()


if __name__ == '__main__':
    main()
