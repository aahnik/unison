#!/bin/bash

# script to auto generate various files

# this script is meant to be run in dev environment

poetry export --without-hashes --format=requirements.txt > requirements.txt
echo "Updated requirements.txt"
npm run build

