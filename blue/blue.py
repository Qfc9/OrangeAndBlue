import os
import platform
import sys
import io
from base64 import b64encode
import eel
import subprocess
import multiprocessing
import psutil
from multiprocessing import Process
import math
import time
import signal

class Connections():
    """
    docstring
    """
    workerp = None

def closeApp(relPath, socks):
    print(relPath)
    print(socks)
    print("It works")

    if len(socks) != 0:
        return

    if allCon.workerp is not None and psutil.pid_exists(allCon.workerp):
        print(os.kill(allCon.workerp, signal.SIGTERM))

    return 0

@eel.expose
def sendit(cpu, ram, server):
    print("SEND IT")
    print(cpu, ram, server)

    if(cpu.isdigit()):
        procs = math.ceil(int(cpu)/4)
        threads = math.ceil(int(cpu)/procs)
        # memory = math.floor(ram/cpu) don't know if limiting the memory per process is needed

        procs = str(procs)
        threads = str(threads)
    else:
        # TODO return logic
        return 0

    args = ["dask-worker.exe", "--tls-ca-file", "certs/myCA.pem", "--tls-cert", "certs/worker.crt", 
            "--tls-key", "certs/worker.key", "--protocol", "tls", "--nprocs", procs, "--nthreads", 
            threads, "--memory-limit", ram+"GB", "tls://"+server+":8786"]
    allCon.workerp = subprocess.Popen(args).pid
    print(allCon.workerp)

    print("IT IS RUNNING")
    return 0

allCon = Connections()

def main():
    eel.init('web')

    eel.start_up(os.cpu_count(), round(((psutil.virtual_memory().total/1024)/1024)/1024))

    try:
        eel.start('index.html', size=(1000, 600), close_callback=closeApp)

    except EnvironmentError:
        print("aaa")
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start('index.html', mode='edge', size=(1000, 600))
        else:
            raise

if __name__ == "__main__":
    main()