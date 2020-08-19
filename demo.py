#!/usr/bin/python3
import time
import progressbar

max=33
for i in range(max+1):
    time.sleep(0.1)
    progressbar.progress(i, max, "This is an demo...")
print("")
