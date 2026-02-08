@echo off
echo ========================================
echo  Bible House Renovation - GitHub Deploy
echo ========================================
echo.
echo Username: bryne_ra
echo Repository: bible-house-reno
echo.
echo This will:
echo  1. Initialize Git repository
echo  2. Add all necessary files
echo  3. Commit changes
echo  4. Push to GitHub
echo.
echo ========================================
echo.

REM Check if git is configured
git config user.name >nul 2>&1
if errorlevel 1 (
    echo Setting up Git configuration...
    set /p NAME="Enter your full name: "
    set /p EMAIL="Enter your GitHub email: "
    git config --global user.name "!NAME!"
    git config --global user.email "!EMAIL!"
)

echo.
echo Step 1: Initializing Git repository...
git init

echo.
echo Step 2: Adding remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/bryne_ra/bible-house-reno.git

echo.
echo Step 3: Adding files...
git add index.html
git add professional_renovation_plan_complete.html
git add README.md
git add .gitignore
git add DEPLOYMENT_GUIDE.md

echo.
echo Step 4: Committing changes...
git commit -m "Initial commit: Bible House Renovation Project with complete documentation and interactive visualizations"

echo.
echo Step 5: Pushing to GitHub...
echo.
echo You will be prompted for your GitHub credentials.
echo.
git branch -M main
git push -u origin main

echo.
echo ========================================
echo  Deployment Complete!
echo ========================================
echo.
echo Your site will be live at:
echo https://bryne_ra.github.io/bible-house-reno/
echo.
echo Next steps:
echo 1. Go to https://github.com/bryne_ra/bible-house-reno
echo 2. Click Settings -^> Pages
echo 3. Under Source, select: main branch
echo 4. Click Save
echo 5. Wait 2-3 minutes
echo.
echo ========================================
pause
