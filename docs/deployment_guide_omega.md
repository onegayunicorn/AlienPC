# 🚀 AlienPC Ω - Full Stack Deployment Guide

## 🎯 Overview
This guide provides instructions for deploying the full AlienPC Ω stack, integrating the high-precision genomics engine with the Akida-accelerated Quadrifecta Protocol.

## 🛠️ Prerequisites
- **OS**: Ubuntu 22.04 LTS (Council Recommended)
- **Python**: 3.11+
- **Hardware**: Akida NPU V2.3.1 (Optional for simulation mode)
- **Node.js**: 22+ (For Plugin Registry)

## 📦 Installation

### 1. Clone the Omega Branch
```bash
git clone https://github.com/onegayunicorn/AlienPC.git
cd AlienPC
git checkout alienpc-omega
```

### 2. Initialize the Environment
```bash
./scripts/init_quadrifecta.sh
pip3 install -r genomics/requirements.txt
```

### 3. Deploy Akida OTA (Phase 1)
```bash
sudo ./phase1-akida-ota/deploy.sh --nodes 40 --hot-swap
```

## 🚀 Running the System

### Start the Genomics API
```bash
python3 genomics/src/api/rest_server.py
```

### Initialize Council Orchestration
```bash
python3 council/orchestrate.py
```

### Start Plugin Registry
```bash
cd phase4-plugin-ecosystem/registry
npm install && node server.js
```

## 🧪 Verification
Run the integrated test suite to ensure all components are harmonized:
```bash
pytest genomics/tests/test_omega_integration.py -v
```

## 🛡️ Security & Maintenance
- **Zero-Trust**: Ensure biometric profiles are synced in `phase3-zero-trust/auth/`.
- **Rollback**: In case of paradox detection, use `./scripts/rollback.sh`.

---
*Sovereign Architect: onegayunicorn*  
*Deployment Version: v1.1.0-omega*
