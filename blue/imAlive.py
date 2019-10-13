import socket
import sys
import os, platform, subprocess, re
import multiprocessing
import tensorflow as tf
from tensorflow.python.client import device_lib
from psutil import virtual_memory
import threading
import pickle
import time

class ImAlive(threading.Thread):
    """docstring for ImAlive."""

    def __init__(self, arg):
        threading.Thread.__init__(self)
        mem = virtual_memory()

        self.id = arg
        self.os = platform.system()
        self.osVer = platform.platform()
        self.cpu = platform.machine()
        self.cpuCount = multiprocessing.cpu_count()
        self.memTotal = mem.total
        # self.gpu = tf.compat.v1.test.is_gpu_available()
        self.gpu = ""
        self.gpuType = ""

        # if self.gpu:
        #     devices = device_lib.list_local_devices()
        #     self.gpuType = devices[1].physical_device_desc

    def run(self):
        while True:
            time.sleep(5)
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 10001)
            print('connecting to %s port %s' % server_address, file=sys.stderr)

            try:
                data = pickle.dumps((self.id, self.os, self.osVer, self.cpu, self.cpuCount, self.memTotal, self.gpu, self.gpuType))
                # Send data
                sock.sendto(data, server_address)

            finally:
                print('closing socket', file=sys.stderr)
                sock.close()
