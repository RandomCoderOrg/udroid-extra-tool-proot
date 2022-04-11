#!/bin/bash


case $(echo "$0" | cut -d "/" -f 4) in
    "startvnc")
        python3 /usr/share/udroid/main.py --startvnc $*
    ;;
    "stopvnc")
        python3 /usr/share/udroid/main.py --stopvnc $*
    ;;
    "udroid-upgrade")
        python3 /usr/share/udroid/main.py --upgrade
    ;;
    "udroid-upgrade-check")
        python3 /usr/share/udroid/main.py --upgrade-check
    ;;
esac
