import torch
from pynvml import *

nvmlInit()

def mem(dev=0):
    h = nvmlDeviceGetHandleByIndex(dev)
    info = nvmlDeviceGetMemoryInfo(h)
    return info.used, info.free, info.total

if __name__ == "__main__":
    used, free, tot = mem(0)
    print (f"{used/tot:.3%} {used:,} bytes out of {tot:,} total; {free:,} free")