#!/usr/bin/python3
import wget
import progressbar
import time

url='https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-10.5.0-amd64-DVD-1.iso'
def bar(current, total, length):
    global current_old
    global time_old
    global n
    n=n+1
    if n == 200:
        current_old, time_old = progressbar.dload(current, total, "test", current_old, time_old)
        n=0

n=0
current_old=0
time_old=time.time()
wget.download(url, bar=bar)
