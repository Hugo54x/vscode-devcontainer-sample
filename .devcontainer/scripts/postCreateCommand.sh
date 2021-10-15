#!/bin/bash
#! pypy is incompatible with certain python libs
apt update &&
# apt install pypy3 -y &&
# apt install python3-pip -y &&
# pypy3 -m pip install --upgrade pip &&
#* sudo-less part
sudo -u vscode python3 -m pip install --upgrade pip &&
sudo -u vscode pip3 install -r ./app/requirements.txt #&&
# pre-commit #* in the moment you have to invoke that comment manually
