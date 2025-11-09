# Setting Up GitHub Repository

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `patchforge-demo`
3. Description: "Vulnerable demo application for PatchForge autonomous security patching"
4. Choose **Public** (so PatchForge can access it)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 2: Connect Local Repo to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
cd /Users/rayansikkandar/patchforge-demo

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/patchforge-demo.git

# Push to GitHub
git push -u origin main
```

## Step 3: Verify

1. Visit `https://github.com/YOUR_USERNAME/patchforge-demo`
2. You should see:
   - `requirements.txt` with vulnerable packages
   - `app.py` Flask application
   - `README.md` with vulnerability list
   - `.gitignore` and `LICENSE`

## Step 4: Test with PatchForge

Once the repo is on GitHub, test PatchForge:

```bash
cd /Users/rayansikkandar/PatchForge
source venv/bin/activate
python main.py
```

When prompted:
1. Enter your GitHub username
2. Select `patchforge-demo` from the list
3. Watch PatchForge scan, patch, and create a PR!

---

**Note:** Make sure your GitHub token has repository permissions in your `.env` file.

