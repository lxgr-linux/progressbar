#!/usr/bin/python3
import time
import os
import sys
import math

max=21
for i in range(max+1):
    time.sleep(0.1)
    width, height = os.get_terminal_size()
    pl=round(math.log(width/57 ,1.01644658))
    #print(str(pl))
    string=' Running singlecore benchmark'+200*' '
    print('\r('+(len(str(max))-len(str(i)))*' '+str(i)+'/'+str(max)+')'+string[:width-16+(6-2*len(str(max)))-pl]+'['+round((i/max)*pl)*'#'+(pl-round((i/max)*pl))*'-'+'] '+(3-len(str(round((i/max)*100))))*' '+str(round((i/max)*100))+'%', end='', flush=True)
print("")
