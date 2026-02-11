# 🔄 AlienPC Migration Guide: v1.0.1 → v2.0.0-omega

## 🎯 Overview
This document outlines the necessary steps to migrate your existing AlienPC v1.0.1 installation to the synthesized AlienPC Ω v2.0.0 architecture.

## ⚠️ Breaking Changes

### 1. Detector Interface
The `SyntheticBaseDetector` has been refactored from a functional interface to a class-based structure to support Akida acceleration states.
- **Old**: `from genomics.src.synthetic_base_detection.detector import detect`
- **New**: `from genomics.src.synthetic_base_detection.detector import SyntheticBaseDetector`

### 2. API Authentication
All REST endpoints now require Zero-Trust JWT authentication. Unauthenticated requests will return `401 Unauthorized`.

## 🛠️ Migration Steps

### Step 1: Update Codebase
```bash
git checkout main
git pull origin main
git merge alienpc-omega
```

### Step 2: Install New Dependencies
```bash
pip install -r requirements.txt --break-system-packages
```

### Step 3: Initialize Akida Hardware Layer
If running on physical nodes with Akida NPU:
```bash
sudo ./phase1-akida-ota/deploy.sh --nodes all --hot-swap
```

### Step 4: Configure Zero-Trust
Update your `genomics/config/api_config.yaml` to include your Council-issued JWT secrets and biometric profiles.

## 🧪 Post-Migration Validation
Run the integration suite to ensure successful migration:
```bash
python3 -m pytest genomics/tests/test_omega_integration.py -v
```

---
*Sovereign Architect: onegayunicorn*  
*Date: 2026-02-11*
