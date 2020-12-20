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

eel.init('web')

test = 1

def spawn(cpu, ram, server):
    print("start of sub")

    if(cpu.isdigit()):
        procs = math.ceil(int(cpu)/4)
        threads = math.ceil(int(cpu)/procs)
        # memory = math.floor(ram/cpu) don't know if limiting the memory per process is needed

        procs = str(procs)
        threads = str(threads)
    else:
        # TODO return logic
        return 0

    subprocess.run("dask-worker.exe --tls-ca-file certs/myCA.pem --tls-cert certs/worker.crt "+
                   "--tls-key certs/worker.key --protocol tls --nprocs "+procs+" "+
                   "--nthreads "+threads+" --memory-limit "+ram+"GB tls://"+server+":8786")
    print("end of sub")

@eel.expose
def sendit(cpu, ram, server):
    print("SEND IT")
    print(cpu, ram, server)
    p = Process(target=spawn, args=(cpu, ram, server), daemon=True)
    p.run()
    return 0

eel.start_up(os.cpu_count(), round(((psutil.virtual_memory().total/1024)/1024)/1024))

try:
    eel.start('index.html', size=(1000, 600))

except EnvironmentError:
    print("aaa")
    # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start('index.html', mode='edge', size=(1000, 600))
    else:
        raise