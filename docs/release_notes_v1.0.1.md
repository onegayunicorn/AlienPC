# AlienPC v1.0.1 - Lumo AI & ChronoForge Release

🚀 **AlienPC is locked in and launch-ready!** This production-grade release introduces the Lumo AI (Claude) integration and the mesmerising ChronoForge-inspired boot sequence.

## ✨ Key Features
- **Lumo AI Assistant**: Privacy-first AI insights integrated directly into the genomics dashboard.
- **ChronoForge Boot Splash**: A deterministic 5-second SVG kaleidoscope sequence with a custom 4-track audio mix.
- **Universal Boot**: Robust support for BIOS and UEFI on legacy and modern hardware.
- **Sovereign Genomics**: Integrated synthetic base detection and nanopore sequencing pipelines.

## 🔒 Security & Privacy
- **Data Sanitization**: Automatic removal of PII before AI processing.
- **Offline-Safe**: `LUMO_PRIVACY_MODE=offline` by default for regulated environments.
- **Integrity**: All ISOs are SHA-256 checksummed and GPG signed.

## 📦 Assets
- `AlienPC.iso`: The full portable OS image.
- `AlienPC.iso.sha256`: SHA-256 checksum for verification.
- `AlienPC.iso.asc`: GPG signature for authenticity.

## 🛠 Quick Start
```bash
# 1. Download & Verify
curl -LO https://github.com/onegayunicorn/AlienPC/releases/latest/download/AlienPC.iso
sha256sum -c AlienPC.iso.sha256
gpg --verify AlienPC.iso.asc AlienPC.iso

# 2. Flash to USB (replace /dev/sdX)
sudo dd if=AlienPC.iso of=/dev/sdX bs=4M status=progress && sync

# 3. Boot & Explore
# Visit http://localhost:8080 after boot
```

## 📖 Documentation
- [README.md](https://github.com/onegayunicorn/AlienPC/blob/main/docs/README.md)
- [Lumo Integration Guide](https://github.com/onegayunicorn/AlienPC/blob/main/docs/lumo-integration.md)
- [Project Roadmap](https://github.com/onegayunicorn/AlienPC/blob/main/docs/roadmap.md)

---
*“One Second = One Epoch. Welcome to the Council.”* 🛸
