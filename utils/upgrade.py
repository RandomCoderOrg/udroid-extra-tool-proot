import os
from utils.funs import *

CURRENT_VERSION = "v0.6"
REMOTE_VERISON = os.popen("git -c 'versionsort.suffix=-' ls-remote --tags --sort='v:refname' https://github.com/RandomCoderOrg/udroid-extra-tool-proot | tail -n1 | cut -d \"/\" -f 3").read().strip()

def isold():
    if CURRENT_VERSION == REMOTE_VERISON:
        return False
    else:
        return True

def isconnected():
    if os.system("ping -W 1 -c 1 github.com >> /dev/null") == 0:
        return True
    else:
        return False

def upgrade_check():
    if isconnected():
        if isold():
            lwarn("You are using an old version of udroid-extra-tool-proot. Please update to the latest version.")
            print("Current version: " + str(CURRENT_VERSION))
            print("Latest version: " + str(REMOTE_VERISON))
            print("[W] You can update by running: "+green("udroid-upgrade"))
        else:
            nmsg("udroid-tools are already on the latest version.")
    else:
        lwarn("You are not connected to the internet. Please connect to the internet and try again.")

def do_upgrade():
    if isconnected():
        if isold():
            print("Upgrading...")
            if os.path.exists("/usr/share/udroid/utils/upgrade.sh"):
                os.system("/usr/share/udroid/utils/upgrade.sh")
            else:
                lwarn("Could not find upgrade script.")
                die  ("Try installing from the official repository.")
        else:
            nmsg("udroid-tools are already on the latest version.")
