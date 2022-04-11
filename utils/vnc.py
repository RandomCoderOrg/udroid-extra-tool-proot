import os
from utils.funs import nmsg

DISPLAY=os.getenv('DISPLAY')
VNC_LOCK_TYPE="/tmp/.X11-unix/X"

def isvncstarted(port:int) -> bool:
    """
    Check if VNC is started
    """
    if os.path.exists(VNC_LOCK_TYPE+str(port)) \
        or os.path.exists("/tmp/.X"+str(port)+"-lock"):
        return True
    else:
        return False

def startvnc(port:int) -> bool:
    """
    Start VNC
    """
    if os.getenv('DEFAULT_VNC_PORT') is not None and os.getenv('DEFAULT_VNC_PORT').isnumeric:
        port=int(os.getenv('DEFAULT_VNC_PORT'))

    if isvncstarted(port):
        return False
    else:
        if os.WEXITSTATUS(os.system("vncserver :"+str(port))) == 0:
            return True
        else:
            return False

def stopvnc(port:int) -> bool:
    """
    Stop VNC
    """
    if os.getenv('DEFAULT_VNC_PORT') is not None and os.getenv('DEFAULT_VNC_PORT').isnumeric:
        port = int(os.getenv('DEFAULT_VNC_PORT'))

    if isvncstarted(port):
        os.WEXITSTATUS(os.system("vncserver -kill :"+str(port)))
        nmsg("Cleaning Lock File")
        if os.path.exists(VNC_LOCK_TYPE+str(port)):
            os.remove(VNC_LOCK_TYPE+str(port))
        if os.path.exists("/tmp/.X"+str(port)+"-lock"):
            os.remove("/tmp/.X"+str(port)+"-lock")
        nmsg("VNC Server Stopped")
    else:
        nmsg("VNC Server not started at "+str(port))
