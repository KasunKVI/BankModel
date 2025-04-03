#!/bin/bash

echo "Post-deployment tasks starting..."

# Navigate to the app directory
cd /home/ec2-user/bank-model

# Install dependencies
pip install -r requirements.txt

# Stop any existing gunicorn processes to avoid conflicts
pkill -f gunicorn

# Start Gunicorn to run the Flask app
nohup gunicorn --bind 0.0.0.0:5000 app:app -D &

echo "Deployment successful" > /home/ec2-user/bank-model/deploy.log


echo "Post-deployment tasks completed."
