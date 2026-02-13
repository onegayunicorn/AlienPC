#!/usr/bin/env bash
# One-click Termux/Linux installer for AlienPC Omega

set -euo pipefail

echo "Initializing AlienPC Omega Setup..."

# Create necessary directories if they don't exist
mkdir -p config logs

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed."
    exit 1
fi

echo "Setup complete. Ready for Omega Evolution."
