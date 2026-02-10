# AlienPC Project Roadmap

## Overview

This document outlines the strategic vision and planned milestones for the AlienPC project. We aim to provide a portable, secure, and AI-augmented OS that empowers researchers and scientists worldwide.

## 📅 Version Milestones

### v1.1 - Q2 2026: Accessibility & Performance
- **Accessibility Variant**: Dynamic "high-contrast" boot splash variant (WCAG 2.1 AA).
- **Expanded Lumo Model**: Integration of `Claude-sonnet-4-2025` for deeper genomics explanations.
- **Local-LLM Fallback**: Full packaging of Ollama within the ISO for 100% offline operation.
- **Telemetry Opt-out**: `BOOT_SPLASH_TELEMETRY=0` environment variable support.

### v1.2 - Q4 2026: Global Reach & Extensibility
- **Multi-language UI**: Localization support for French, Spanish, and Mandarin.
- **Plugin System**: Modular architecture for third-party analysis pipelines.
- **Remote Updates**: Secure, signed Over-The-Air (OTA) update mechanism.

### v2.0 - 2027: Enterprise Security & Reporting
- **Full-Disk Encryption**: LUKS + TPM 2.0 support for user data protection.
- **Automated Reporting**: Integrated "Genome-to-Report" PDF generator with Lumo AI summaries.
- **Community Marketplace**: Portal for custom boot-splash themes and analysis modules.

## 🤝 Contributing to the Roadmap

We welcome community feedback on these milestones. If you have a feature request or would like to contribute to a specific target:
1. Open a **Feature Request** issue on GitHub.
2. Tag your PR with the corresponding version milestone (e.g., `v1.1-candidate`).
3. Ensure all new features include updated documentation in `docs/`.

---
*Last Updated: February 10, 2026*
