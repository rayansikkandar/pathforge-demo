# 🚨 Vulnerable Demo Application

**WARNING: This application contains INTENTIONAL security vulnerabilities for demonstration purposes.**

## Known Vulnerabilities

This project uses outdated packages with real CVEs:

| Package | Version | CVE | CVSS | Issue |
|---------|---------|-----|------|-------|
| Flask | 2.0.1 | CVE-2023-30861 | 9.8 | Cookie parsing vulnerability |
| PyYAML | 5.3.1 | CVE-2020-14343 | 9.8 | Arbitrary code execution |
| Werkzeug | 2.0.0 | CVE-2023-25577 | 7.5 | Path traversal |
| Jinja2 | 2.11.3 | CVE-2024-22195 | 6.1 | XSS vulnerability |
| cryptography | 3.3.2 | CVE-2023-23931 | 6.5 | Cipher weakness |
| requests | 2.25.1 | CVE-2023-32681 | 6.1 | Proxy auth leak |
| urllib3 | 1.26.4 | CVE-2023-43804 | 5.9 | Cookie leak |

## Purpose

This repository is designed to demonstrate **PatchForge**, an autonomous security patching agent that:

1. Scans dependencies for vulnerabilities
2. Researches secure versions
3. Generates patches automatically
4. Validates the fixes
5. Creates pull requests

## DO NOT Deploy

**Never deploy this application to production.** It exists solely for security tooling demonstrations.

## Fixing Vulnerabilities

To see PatchForge in action:

```bash
python main.py
# Enter username when prompted
# Select this repository
# Watch autonomous patching happen
```

## Manual Fix

To manually update dependencies:

```bash
pip install --upgrade Flask Werkzeug PyYAML Jinja2 cryptography requests urllib3
pip freeze > requirements.txt
```

---

Created for UTD Hack 2025 - NVIDIA Nemotron Prize Track
