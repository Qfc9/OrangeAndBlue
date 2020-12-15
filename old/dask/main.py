# import dask.array as da
# from distributed.client import *
# import time
# from dask.distributed import Client, LocalCluster
#
# def main():
#     x = da.random.random((10000, 10000, 10), chunks=(1000, 1000, 5))
#     y = da.random.random((10000, 10000, 10), chunks=(1000, 1000, 5))
#     z = (da.arcsin(x) + da.arccos(y)).sum(axis=(1, 2))
#     z.compute()
#
# if __name__ == '__main__':
#     # cluster = LocalCluster()
#     client = Client("127.0.0.1:8786")
#     main()


import dask
from dask.distributed import Client
import numpy as np

@dask.delayed
def inc(x):
    return x + 1

@dask.delayed
def double(x):
    return x + 2

@dask.delayed
def add(x, y):
    return x + y

def main():
    client = Client("127.0.0.1:8786")
    data = np.array([1, 2, 3, 4, 5])

    output = []
    for x in data:
        a = inc(x)
        b = double(x)
        c = add(a, b)
        output.append(c)

    total = dask.delayed(sum)(output)
    print(total.compute())

if __name__ == '__main__':
    main()

# from dask.distributed import Client
#
# client = Client()
#
#
# def inc(x):
#     sleep(random.random() / 10)
#     return x + 1
#
# def dec(x):
#     sleep(random.random() / 10)
#     return x - 1
#
# def add(x, y):
#     sleep(random.random() / 10)
#     return x + y
#
#
# e = Executor('127.0.0.1:8786')
#
# incs = e.map(inc, range(100))
# decs = e.map(dec, range(100))
# adds = e.map(add, incs, decs)
# total = e.submit(sum, adds)
#
# del incs, decs, adds
# total.result()
# total.compute()
