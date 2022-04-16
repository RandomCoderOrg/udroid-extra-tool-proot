import os, time

CLIPBOARD_BUFFER_FILE="/tmp/clipboard"

##############
# watch if clipboard buffer file has changed with last modified time
# if changed, then copy the content to clipboard
def start_clipboard_service():
    last_modified_time = os.path.getmtime(CLIPBOARD_BUFFER_FILE)
    # check is xclip installed
    _xclip = os.popen("which xclip").read().strip()
    if _xclip is None:
        print("xclip not found")
        os.exit(1)
    
    while os.get('Display') is not None:
        time.sleep(0.4)
        if os.path.exists(CLIPBOARD_BUFFER_FILE):
            if os.path.getmtime(CLIPBOARD_BUFFER_FILE) != last_modified_time:
                os.system(f"cat {CLIPBOARD_BUFFER_FILE} | xclip -selection clipboard")
        else:
            print("clipboard buffer file not found")
            os.exit(1)
