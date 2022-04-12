import os
from utils.funs import *

######## VNC
if os.popen("hostname -I | cut -d \" \" -f 2 | tr -d '\\n'").read() is '':
    # hostname returs \n which can effect logic
    IPv4Address = os.popen("hostname -I | tr -d '\\n'").read().strip()
else:
    IPv4Address = os.popen("hostname -I | cut -d \" \" -f 2 | tr -d '\\n'").read().strip()

LOCALIP="127.0.0.1"

def vncokdialog(port):
    return "vncserver started on "\
        +"\n"+magneta(str(LOCALIP)+":"+str(port))\
        +"\n"+magneta(str(IPv4Address)+":"+str(port))\
        +"\n"+"To stop it, run:\n"\
        +green("vncserver -kill :"+str(port))\
        +" or "+blue("stopvnc")

def vncrunningdialog(port):
    return "vncserver already started on "\
        +"\n"+magneta(str(LOCALIP)+":"+str(port))\
        +"\n"+magneta(str(IPv4Address)+":"+str(port))\
        +"\n"+"To stop it, run:\n"\
        +green("vncserver -kill :"+str(port))\
        +" or "+blue("stopvnc")
