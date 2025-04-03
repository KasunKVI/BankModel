#!/bin/bash
cd /home/ec2-user/bankmodel
pip install -r requirements.txt
pkill -f flask
nohup python app.py > app.log 2>&1 &
