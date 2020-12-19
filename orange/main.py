import socket
import sys
import pickle
import traceback
import dask
from dask.distributed import Client
import dask.array as da
from distributed.security import Security


def main():
    print("Orange")

    sec = Security(tls_ca_file='certs/myCA.pem',
                tls_client_cert='certs/scheduler.crt',
                tls_client_key='certs/scheduler.key',
                require_encryption=True)

    client = Client("tls://192.168.1.151:8786", security=sec)  # Connect to distributed cluster and override default
    x = da.random.random((40000, 40000), chunks=(1000, 1000))  # This now runs on the distributed system

    y = da.exp(x).sum()

    print(y.compute())


if __name__ == "__main__":
    main() 