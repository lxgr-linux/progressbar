#!/usr/bin/python3
import wget
import progressbar
import time

url='https://osdn.net/frs/redir.php?m=dotsrc&f=%2Fstorage%2Fg%2Fm%2Fma%2Fmanjaro%2Fxfce%2F20.0.3%2Fmanjaro-xfce-20.0.3-200606-linux56.iso'
def bar(current, total, length):
    global current_old
    global time_old
    current_old, time_old = progressbar.dload(current, total, "test", current_old, time_old)
current_old=0
time_old=time.time()
wget.download(url, bar=bar)
