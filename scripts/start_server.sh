#!/bin/bash
cd /home/ec2-user/bank-model
pip install -r requirements.txt
pkill -f gunicorn
gunicorn --bind 0.0.0.0:5000 app:app -D
