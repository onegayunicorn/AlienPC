#!/usr/bin/env bash
# Run after the rootfs is mounted
systemctl start networking.service
nohup python3 /opt/alienpc/genomics/src/api/rest_server.py > /var/log/alienpc_api.log 2>&1 &

# Add other service startup commands here

echo "AlienPC services started."
