#!/usr/bin/env bash
# Master launcher for Termux AI pipelines

set -euo pipefail

# Load API keys (if you stored them in config/api_keys.env)
if [[ -f "$(dirname "$0")/../config/api_keys.env" ]]; then
  source "$(dirname "$0")/../config/api_keys.env"
fi
