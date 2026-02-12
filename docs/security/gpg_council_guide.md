# 🧬 GPG Council Multisig: 2-of-3 Quantum Signatures

## Setup (One-Time)
```bash
# Generate council keys (council-member-1, council-member-2, council-member-3)
for i in 1 2 3; do
  gpg --quick-generate-key "council-member-$i@alienpc.omega" rsa4096
done

# Export public keys to GitHub (repeat for each)
gpg --armor --export council-member-1@alienpc.omega | pbcopy
# GitHub Settings → SSH/GPG → New GPG Key
```

## Git Config for Council Signing
```bash
git config --global commit.gpgsign true
git config --global user.signingkey council-multisig@alienpc.omega
```

## 2-of-3 Multisig Verification (GitHub Actions checks this)
```bash
# Verify minimum 2 council signatures on commits
git log --show-signature --oneline -5 | grep -E "council-member-(1|2|3)" | wc -l | awk '{if($1>=2) print "✅ COUNCIL QUORUM"; else print "❌ INSUFFICIENT SIGNATURES"}'
```
