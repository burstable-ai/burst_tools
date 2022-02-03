import sys
import argparse
# import torch
from pynvml import *

nvmlInit()

def mem(dev=0):
    h = nvmlDeviceGetHandleByIndex(dev)
    info = nvmlDeviceGetMemoryInfo(h)
    return info.used, info.free, info.total

if __name__ == "__main__":
    dev = 0
    if len(sys.argv) > 1:
        dev = int(sys.argv[1])
    devs = nvmlDeviceGetCount()
    if dev >= devs:
        raise Exception(f"No such device; {devs} devices available")
    used, free, tot = mem(dev)
    print (f"{used/tot:.3%} {used/1000000:.3f}mb out of {tot/1000000:.3f}mb free: {free/1000000:.3f}mb")