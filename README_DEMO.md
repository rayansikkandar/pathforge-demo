# 🎯 PatchForge Demo Repository

This repository is **intentionally vulnerable** and designed to demonstrate PatchForge's autonomous security patching capabilities.

## 🚨 Warning

**DO NOT deploy this application to production.** It contains real security vulnerabilities for demonstration purposes only.

## 📦 Vulnerable Packages

This demo includes 7 packages with known CVEs:

| Package | Version | CVE | CVSS | Severity |
|---------|---------|-----|------|----------|
| Flask | 2.0.1 | CVE-2023-30861 | 9.8 | CRITICAL |
| PyYAML | 5.3.1 | CVE-2020-14343 | 9.8 | CRITICAL |
| Werkzeug | 2.0.0 | CVE-2023-25577 | 7.5 | HIGH |
| cryptography | 3.3.2 | CVE-2023-23931 | 6.5 | MEDIUM |
| Jinja2 | 2.11.3 | CVE-2024-22195 | 6.1 | MEDIUM |
| requests | 2.25.1 | CVE-2023-32681 | 6.1 | MEDIUM |
| urllib3 | 1.26.4 | CVE-2023-43804 | 5.9 | MEDIUM |

## 🎬 Running the Demo

### Step 1: Push to GitHub

```bash
# If not already on GitHub:
./setup_github.sh
# Or follow SETUP_GITHUB.md
```

### Step 2: Run PatchForge

```bash
cd ../PatchForge
source venv/bin/activate
python main.py
```

### Step 3: Select This Repository

1. Enter your GitHub username
2. Select `patchforge-demo` from the list
3. Press Enter to start

### Step 4: Watch the Magic

PatchForge will:
1. 🔍 Scan dependencies for vulnerabilities
2. 🔬 Research secure versions
3. 🔧 Generate patches
4. 🧪 Validate the fixes
5. 📝 Create a pull request

## 📊 Expected Results

- **Scan time**: ~10-15 seconds
- **Vulnerabilities found**: 7+ CVEs
- **Patches generated**: Multiple security fixes
- **Validation**: All checks passed
- **PR created**: Ready for review

## 🔗 Related Documentation

- **PatchForge Main Repo**: See `../PatchForge/README.md`
- **Demo Script**: See `../PatchForge/DEMO_SCRIPT.md`
- **Before/After**: See `../PatchForge/BEFORE_AFTER.md`
- **Quick Start**: See `../PatchForge/QUICK_START.md`

## 🎓 For Judges/Demo

This repository is designed to showcase:
- ✅ Real vulnerabilities (not mock data)
- ✅ Autonomous detection and patching
- ✅ Professional PR generation
- ✅ Full validation pipeline
- ✅ Zero human intervention

## 📝 Files

- `requirements.txt` - Vulnerable dependencies
- `app.py` - Simple Flask application
- `README.md` - Repository documentation
- `.gitignore` - Git ignore rules
- `LICENSE` - MIT License

---

**Created for UTD Hack 2025 - NVIDIA Nemotron Prize Track**

