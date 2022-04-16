import os
import sys
import optparse
from utils.info import *
from utils.funs import *

def vnc_mode(port=1,mode="start",xstartup=os.getenv('HOME')+"/.vnc/xstartup"):
    import utils.vnc as vnc
    
    if os.path.exists(xstartup):
        if mode == "start":
            if vnc.startvnc(port):
                print(vncokdialog(port))
            else:
                print(vncrunningdialog(port))
        elif mode == "stop":
            vnc.stopvnc(port)
    else:
        print("xstartup file not found")

if __name__ == '__main__':
    parser =  optparse.OptionParser()
    parser.add_option("--clipboard-service", action="store_true", dest="clipboard_service", default=False, help="Start clipboard service")
    parser.add_option("--upgrade"   ,action="store_true", default=False, help="Installs update if found updates")
    parser.add_option("--upgrade-check",action="store_true", default=False, help="check for updates")
    parser.add_option("--startvnc"  ,action='store_true', default=False, help="Start VNC on port")
    parser.add_option("--stopvnc"   ,action='store_true', default=False, help="Stop VNC on port")
    parser.add_option("-p", "--port", help="VNC port" , default=1)

    (options, args) = parser.parse_args()

    if options.startvnc:
        vnc_mode(port=options.port,mode="start")
        sys.exit(0)
    if options.stopvnc:
        vnc_mode(port=options.port,mode="stop")
        sys.exit(0)
    if options.upgrade:
        from utils.upgrade import *
        do_upgrade()
        sys.exit(0)
    if options.upgrade_check:
        from utils.upgrade import *
        upgrade_check()
        sys.exit(0)
    if options.clipboard_service:
        from utils.clipboard_watcher import *
        start_clipboard_service()
