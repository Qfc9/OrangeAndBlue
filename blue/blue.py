import os
import platform
import sys
import io
from base64 import b64encode
import eel
import subprocess
from multiprocessing import Process

eel.init('web')

def spawn():
    print("start of sub")
    subprocess.run("dask-worker.exe 192.168.1.151:8786")
    print("end of sub")

@eel.expose
def sendit():
    print("SEND IT")
    p = Process(target=spawn, daemon=True)
    p.run()
    return 0

# @eel.expose
# def dummy(dummy_param):
#     print("I got a parameter: ", dummy_param)
#     return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}


# @eel.expose
# def generate_qr(data):
#     img = pyqrcode.create(data)
#     buffers = io.BytesIO()
#     img.png(buffers, scale=8)
#     encoded = b64encode(buffers.getvalue()).decode("ascii")
#     print("QR code generation successful.")
#     return "data:image/png;base64, " + encoded


# eel.start('index.html', size=(1000, 600))
# Launching Edge can also be gracefully handled as a fall back
try:
    eel.start('index.html', mode='chrome-app', size=(1000, 600))
except EnvironmentError:
    # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start('index.html', mode='edge', size=(1000, 600))
    else:
        raise