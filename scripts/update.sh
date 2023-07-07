#!/bin/bash

shopt -s expand_aliases
source ~/.bash_aliases

git fetch && git pull

echo "Do you want to create a fresh virtual environment ?"
read -r fresh

if [ "$fresh" == "y" ]; then
    echo "Deleting old venv if any"
    rm -rf .venv
    echo "Creating new venv"
    python -m venv .venv
fi

source .venv/bin/activate

pip install -r requirements.txt

