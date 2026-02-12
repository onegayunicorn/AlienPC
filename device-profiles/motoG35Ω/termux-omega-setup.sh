#!/data/data/com.termux/files/usr/bin/bash
pkg update && pkg upgrade -y
pkg install python git gnupg openssl termux-api -y
pip install PyGithub python-gnupg requests

mkdir -p /sdcard/alienpc/{healing_queue,audit,quarantine}
cd /sdcard/alienpc

# Clone Omega branch
git clone -b omega-evolution https://github.com/onegayunicorn/AlienPc.git

echo "✅ MotoG35Ω Omega-ready"
echo "🔐 GPG Key: D8019C31DF90736819FC15A381DBE11A561ECC62"
echo "🌐 Branch: omega-evolution"
