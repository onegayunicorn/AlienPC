#!/usr/bin/env bash
# Run after the rootfs is mounted
# Ensure systemd is aware of new service files
systemctl daemon-reload

# Enable and start the genomics service
systemctl enable --now alienpc-genomics.service

# Start networking
systemctl start networking.service

echo "AlienPC services started and genomics engine is online."
