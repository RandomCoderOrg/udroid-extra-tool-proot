import os, time

CLIPBOARD_BUFFER_FILE="/tmp/clipboard"

##############
# watch if clipboard buffer file has changed with last modified time
# if changed, then copy the content to clipboard
def start_clipboard_service():
    buffer=os.popen(f"cat {CLIPBOARD_BUFFER_FILE}").read().strip()
    
    # check is xclip installed
    _xclip = os.popen("which xclip").read().strip()
    if _xclip is None:
        print("xclip not found")
        os.exit(1)
    
    while os.getenv('DISPLAY') is not None:
        time.sleep(0.4)
        if os.path.exists(CLIPBOARD_BUFFER_FILE):
            if buffer!=os.popen(f"cat {CLIPBOARD_BUFFER_FILE}").read().strip():
                os.system(f"cat {CLIPBOARD_BUFFER_FILE} | xclip -selection clipboard")
                buffer=os.popen(f"cat {CLIPBOARD_BUFFER_FILE}").read().strip()
        else:
            print("clipboard buffer file not found")
            os.exit(1)
        
