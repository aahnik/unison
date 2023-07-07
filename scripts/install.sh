#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3.11 python3.11-venv nginx net-tools -y
git clone https://github.com/aahnik/temple-web.git
cd temple-web || { echo "Directory temple-web not found"; exit; }
alias python=python3.11
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

