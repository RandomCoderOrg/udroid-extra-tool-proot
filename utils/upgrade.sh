#!/bin/bash

repo_link="https://github.com/RandomCoderOrg/udroid-extra-tool-proot"
_basename="$(basnemae $repo_link)"
if [ -d "$_basename" ]; then
    rm -rf "$_basename"
fi

git clone "$repo_link"
cd "$_basename" || exit 1
bash install.sh
