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
import requests
import zipfile
from os import path

class Connections():
    """
    docstring
    """
    workerp = None

def close_app(relPath, socks):
    print(relPath)
    print(socks)
    print("Closing Selene...")

    if len(socks) != 0:
        return

    close_worker()
    exit()

@eel.expose
def py_get_config():
    config = ""
    with open(".config.json", "r") as fjson:
        config = fjson.read()

    eel.js_get_config(config)
    return

@eel.expose
def update_app(update_link, restart):
    print("Updating app...")

    current_process = psutil.Process()
    children = current_process.children(recursive=True)
    for child in children:
        print('Child pid is {}'.format(child.pid))

    print("END")

    print(update_link)
    print(restart)

    if path.exists('downloads') is False:
        try:
            os.mkdir("downloads") 
        except Exception as e:
            print("Update stopped. Can't create downloads folder.")
            print(e)
            return

    r = requests.get(update_link, allow_redirects=True)

    open('downloads/update.zip', 'wb').write(r.content)

    with zipfile.ZipFile("downloads/update.zip", 'r') as zip_ref:
        zip_ref.extractall(".")

    if restart:
        args = ["update.exe", "localhost:1111"]
        try:
            subprocess.Popen(args)
        except Exception as e:
            print("Update FAILED. Can't execute update.exe.")
            print(e)
            eel.finished_update()
            return

        eel.close_app()
        close_worker()
        print("EXIT")
        sys.exit("Forced restart for update")

    eel.finished_update()
    print("Update done")
    

@eel.expose
def launch_worker(cpu, ram, server):
    print("Launching worker...")
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
    print("Worker's PID:", allCon.workerp)

    return 0

@eel.expose
def close_worker():
    print("Closing worker")

    if allCon.workerp is not None and psutil.pid_exists(allCon.workerp):
        os.kill(allCon.workerp, signal.SIGTERM)
    else:
        print("No worker to close")
        return

    print("Worker Closed")

allCon = Connections()

def main():
    eel.init('web')

    eel.start_up(os.cpu_count(), round(((psutil.virtual_memory().total/1024)/1024)/1024))

    try:
        eel.start('index.html', size=(1000, 600), close_callback=close_app)

    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start('index.html', mode='edge', size=(1000, 600), close_callback=close_app)
        else:
            raise

if __name__ == "__main__":
    main()