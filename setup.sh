#!/bin/bash

echo 'Setting up env and packages...'
virtualenv env
source ./env/bin/activate
pip install -r requirements.txt
echo 'Done!'