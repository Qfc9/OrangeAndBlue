import socket
import sys
import os, platform, subprocess, re
import multiprocessing
import imAlive
import getId

def main():
    id = 0
    print("Loaded Blue")

    while id == 0:
        id = getId.getId()

    print(id)

    thread1 = imAlive.ImAlive(id)
    thread1.start()


if __name__ == '__main__':
    main()
