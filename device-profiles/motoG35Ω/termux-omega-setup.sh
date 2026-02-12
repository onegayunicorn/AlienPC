#!/data/data/com.termux/files/usr/bin/bash
# MotoG35Ω: Full Omega Sync System

set -e

echo "🛰️ MotoG35Ω Ω-Sync Initializing..."

# 1. Install dependencies
pkg update -y && pkg install git python gpg openssh -y

# 2. Clone/pull AlienPC
git config --global user.email "motog35@alienpc.omega"
git config --global user.signingkey motog35-council@alienpc.omega
git config --global commit.gpgsign true

if [ ! -d AlienPc ]; then
  git clone https://github.com/onegayunicorn/AlienPc.git
  cd AlienPc
else
  cd AlienPc
  git checkout omega-evolution
  git pull origin omega-evolution
fi

# 3. Setup council GPG (import from repo)
mkdir -p ~/.gnupg
gpg --import docs/security/council_public_keys.asc

# 4. Sync healing logs → council
mkdir -p device-logs/genomics-logs
# TODO: rsync or adb pull from /sdcard/healing-logs

# 5. Run council dashboard simulation
python council/simulations/kaleidoscope/council_dashboard.py

echo "✅ MotoG35Ω synced to council. Ready for protocols."
echo "Next: ./device-profiles/motoG35Ω/deploy_protocol.sh <protocol-name>"
