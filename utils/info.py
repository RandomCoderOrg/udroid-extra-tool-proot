import socket
from funs import *

######## VNC
IPv4Address=socket.gethostbyname(socket.gethostname())
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

print(vncokdialog(5900))
print(IPv4Address)
print(socket.gethostbyname(socket.gethostname()))


