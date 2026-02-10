#!/usr/bin/env bash
# Detect the first removable block device and mount it at /mnt/alienpc

set -euo pipefail

DEV=$(lsblk -rpno NAME,TYPE | awk '$2=="disk" && $1!="/dev/sda"{print $1}' | head -n1)

if [[ -z "$DEV" ]]; then
  echo "No removable device found."
  exit 1
fi

mkdir -p /mnt/alienpc
mount "${DEV}1" /mnt/alienpc || {
  echo "Failed to mount $DEV"
  exit 1
}
echo "Mounted ${DEV}1 at /mnt/alienpc"
