import socket
import sys
import os, platform, subprocess, re
import multiprocessing
import tensorflow as tf
from tensorflow.python.client import device_lib
from psutil import virtual_memory
import threading

class ImAlive(threading.Thread):
    """docstring for ImAlive."""

    def __init__(self):
        threading.Thread.__init__(self)
        mem = virtual_memory()

        self.os = platform.system()
        self.osVer = platform.platform()
        self.cpu = platform.machine()
        self.cpuCount = multiprocessing.cpu_count()
        self.memTotal = mem.total
        self.gpu = tf.compat.v1.test.is_gpu_available()

        if self.gpu:
            devices = device_lib.list_local_devices()
            self.gpuType = devices[1].physical_device_desc

    def run(self):
        for xxx in range(10000000):
            pass
        print("It works")
