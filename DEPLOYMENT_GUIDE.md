# 🚀 GitHub Pages Deployment Guide

## Step-by-Step Instructions

### 1️⃣ Create GitHub Account (if you don't have one)
- Go to https://github.com
- Click "Sign up"
- Follow the registration process

### 2️⃣ Create New Repository
1. Click the "+" icon (top right) → "New repository"
2. Repository name: `bible-house-reno` (or any name you prefer)
3. Description: "Bible House Renovation Project Documentation"
4. Choose: **Public** (required for free GitHub Pages)
5. ✅ Check "Add a README file" (optional, we have one)
6. Click "Create repository"

### 3️⃣ Upload Files

**Option A: Using Web Interface (Easiest)**
1. In your repository, click "Add file" → "Upload files"
2. Drag and drop these files:
   - `index.html` (landing page)
   - `professional_renovation_plan_complete.html` (main project)
   - `README.md` (project description)
3. Scroll down, add commit message: "Initial project upload"
4. Click "Commit changes"

**Option B: Using Git Desktop (If you prefer GUI)**
1. Download GitHub Desktop: https://desktop.github.com
2. Clone your repository
3. Copy all files to the cloned folder
4. Commit and push

**Option C: Using Command Line**
```bash
# Navigate to your project folder
cd "c:\Users\LENOVO\OneDrive\Documents\bible house reno"

# Initialize git (if not already)
git init

# Add remote repository (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/bible-house-reno.git

# Add all files
git add .

# Commit
git commit -m "Initial commit: Bible House Renovation Project"

# Push to GitHub
git branch -M main
git push -u origin main
```

### 4️⃣ Enable GitHub Pages
1. In your repository, go to **Settings** (top right)
2. Click **Pages** (left sidebar)
3. Under "Source":
   - Branch: Select **main**
   - Folder: Select **/ (root)**
4. Click **Save**
5. Wait 2-3 minutes for deployment

### 5️⃣ Access Your Site
Your site is live at:
```
https://bryne-ra.github.io/bible-house-reno/
```

Key pages:
```
Home: https://bryne-ra.github.io/bible-house-reno/
Guide: https://bryne-ra.github.io/bible-house-reno/overview.html
Before/After: https://bryne-ra.github.io/bible-house-reno/beforeafter.html
Complete: https://bryne-ra.github.io/bible-house-reno/professional_renovation_plan_complete.html
```

---

## ⚠️ Important Notes

### File Size Consideration
- Your `professional_renovation_plan_complete.html` is **56MB**
- GitHub allows files up to **100MB**
- ✅ You're good to go!
- First load may take 10-20 seconds (one-time download)
- After that, browser caches it

### If Upload Fails (File Too Large)
If GitHub rejects the 56MB file:

1. **Use Git LFS (Large File Storage)**
   ```bash
   git lfs install
   git lfs track "*.html"
   git add .gitattributes
   git add professional_renovation_plan_complete.html
   git commit -m "Add large HTML file"
   git push
   ```

2. **Or split the file** (I can help with this)

### Custom Domain Setup (Optional)
If you want to use your own domain later instead of the GitHub Pages URL:

**Step 6: Configure Custom Domain**

1. Purchase a domain (e.g., biblehouse-reno.com) from a registrar like Cloudflare or Namecheap

2. In GitHub repository Settings → Pages → Custom domain, enter your domain (e.g., www.biblehouse-reno.com)

3. In your domain registrar's DNS settings, add a **CNAME record**:
   - **Type:** CNAME
   - **Name:** www
   - **Value:** bryne-ra.github.io
   - **TTL:** 3600 (or default)

4. Wait 24-48 hours for DNS propagation (usually much faster)

5. GitHub will automatically issue an HTTPS certificate

For more details, see: [GitHub's DNS Configuration Guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

---

## 🎉 You're Done!

Your site is live at: **https://bryne-ra.github.io/bible-house-reno/**

Share your project link with anyone. They can:
- ✅ View on any device
- ✅ Interact with before/after sliders
- ✅ Download the page offline
- ✅ No ads, no tracking
- ✅ 100% free forever

---

## 🆘 Need Help?

If you get stuck, let me know at which step!
