#!/bin/bash

# Example post-deploy script
echo "Post-deployment tasks starting..."

# Run any other post-deployment logic here
echo "Deployment successful" > /home/ec2-user/bankmodel/deploy.log

# Example: Restarting a service if necessary
# sudo systemctl restart some-service

echo "Post-deployment tasks completed."
