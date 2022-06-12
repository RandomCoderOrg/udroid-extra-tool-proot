#!/bin/bash

# #############################################################################
#  (C) @RandomCoderOrg @SaicharanKandukuri 2022
#  A useradd wrapper to add a new non-root user for proot linux container
# #############################################################################

REQUIRED_DEPS="openssl useradd"

# sudo check
[[ $EUID -ne 0 ]] && die "You need to be root to run this script"

# check for dependencies
for debs in $REQUIRED_DEPS; do
    if ! dpkg -s "$debs" >/dev/null 2>&1; then
        echo "Missing dependency: $debs"
    fi
done

# check for arguments
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 [ -u | --user | --username ] <username> [ -p | --passwd | --password ] <password> [options]"
    echo "options:"
    echo "--nopasswd -> do not set a password"
    exit 1
fi

while [[ $# -gt 0 ]]; do
    case $1 in
    -u | --user | --username)
        USERNAME="$2"
        shift
        ;;
    -p | --passwd | --password)
        PASSWORD="$2"
        shift
        ;;
    --nopasswd) NOPASSWD=true ;;
    esac
done

if [ -d /home/$USERNAME ]; then
    echo "User $USERNAME already exists"
    exit 1
fi

echo "creating user $USERNAME"
if $NOPASSWD; then
    useraddd -m -G sudo -d /home/"$USERNAME" -k /etc/skel -s "$SHELL" "$USERNAME"
    echo "Adding user $USERNAME to sudoers "
    echo "$USERNAME" ALL=\(root\) ALL >/etc/sudoers.d/"$USERNAME"
    chmod 0440 /etc/sudoers.d/"$USERNAME"
else
    useraddd -m -G sudo -p "$(openssl passwd -1 "$PASSWORD")" -d /home/"$USERNAME" -k /etc/skel -s "$SHELL" "$USERNAME"
    echo "Adding user $USERNAME to sudoers"
    echo "$USERNAME" ALL=\(root\) NOPASSWD: ALL >/etc/sudoers.d/"$USERNAME"
    chmod 0440 /etc/sudoers.d/"$USERNAME"
fi

echo "Done"
