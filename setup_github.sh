#!/bin/bash

# Setup script to push patchforge-demo to GitHub

set -e

echo "🚀 Setting up patchforge-demo GitHub repository"
echo ""

# Check if we're in the right directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: This script must be run from the patchforge-demo directory"
    exit 1
fi

# Get GitHub username
read -p "Enter your GitHub username: " GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Error: GitHub username is required"
    exit 1
fi

echo ""
echo "📋 Steps to complete:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   - Go to: https://github.com/new"
echo "   - Name: patchforge-demo"
echo "   - Description: Vulnerable demo application for PatchForge"
echo "   - Make it PUBLIC"
echo "   - DO NOT initialize with README, .gitignore, or license"
echo "   - Click 'Create repository'"
echo ""
read -p "Press ENTER when you've created the repository on GitHub..."

# Check if remote already exists
if git remote | grep -q origin; then
    echo "⚠️  Remote 'origin' already exists. Updating..."
    git remote set-url origin "https://github.com/${GITHUB_USERNAME}/patchforge-demo.git"
else
    echo "➕ Adding GitHub remote..."
    git remote add origin "https://github.com/${GITHUB_USERNAME}/patchforge-demo.git"
fi

# Push to GitHub
echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Done! Your repository is now at:"
echo "   https://github.com/${GITHUB_USERNAME}/patchforge-demo"
echo ""
echo "🧪 Next steps:"
echo "   1. Test PatchForge: cd ../PatchForge && python main.py"
echo "   2. Select 'patchforge-demo' when prompted"
echo "   3. Watch it create a security patch PR!"

