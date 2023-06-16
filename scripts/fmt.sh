#!/bin/bash

# activate virtual enviroment
source .venv/bin/activate

# run black and isort
black .
isort .
