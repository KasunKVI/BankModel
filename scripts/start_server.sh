#!/bin/bash

echo "Starting server..."

cd /home/ec2-user/bank-model

# Ensure all dependencies are installed
pip install -r requirements.txt

# Start Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app -D

echo "Server started."
