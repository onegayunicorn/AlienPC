#!/bin/bash
# FULL council GPG automation
set -e

echo "🧬 Initializing AlienPC Council GPG Multisig..."

# Generate 3 council keys
for i in 1 2 3; do
  gpg --batch --generate-key <<EOF2
Key-Type: RSA
Key-Length: 4096
Subkey-Type: RSA
Subkey-Length: 4096
Name-Real: council-member-$i
Name-Email: council-member-$i@alienpc.omega
Expire-Date: 0
Passphrase: 
%commit
EOF2
done

echo "✅ Council keys generated. Export to GitHub manually."
echo "Next: git config --global commit.gpgsign true"
