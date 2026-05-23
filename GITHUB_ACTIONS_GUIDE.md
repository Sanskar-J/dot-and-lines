# GitHub Actions APK Build Guide

## Step 1: Create GitHub Account (if you don't have one)
1. Go to: https://github.com/
2. Click **Sign up**
3. Fill in email, password, username
4. Verify your email

---

## Step 2: Create New Repository

1. After logging in, click **+** (top right) → **New repository**
2. Fill in:
   - **Repository name:** `DotsAndBoxes` (or any name)
   - **Description:** "Dots and Boxes Game"
   - **Public** or **Private** (your choice)
   - ✓ Check "Add a README file"
3. Click **Create repository**

---

## Step 3: Upload Your Files to GitHub

### Using GitHub Web Interface (Easiest):

1. Click **Add file** → **Upload files**
2. Drag & drop these files from `c:\SanskarDE\`:
   - `main.py`
   - `buildozer.spec`
   - `.github/workflows/build.yml` (already created)

3. Click **Commit changes**

### OR Using Git Command Line (Advanced):

```bash
cd c:\SanskarDE
git init
git add .
git commit -m "Initial commit - Dots and Boxes game"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/DotsAndBoxes.git
git push -u origin main
```

(Replace `YOUR_USERNAME` with your GitHub username)

---

## Step 4: Trigger the Build

The APK builds automatically when you push code. To watch it:

1. Go to your GitHub repo
2. Click **Actions** tab (top)
3. You'll see "Build APK" workflow running
4. Wait 10-15 minutes for completion

---

## Step 5: Download Your APK

1. In the **Actions** tab, click the completed **Build APK** run
2. Scroll down to **Artifacts**
3. Click **apk-artifact** to download
4. Extract the `.zip` file
5. Inside you'll find: `dotsandboxes-0.1-debug.apk`

---

## Step 6: Install on Android Phone

1. **Transfer APK to your phone** (email, USB, cloud storage, etc.)
2. **On phone:** Settings → Security → Enable "Unknown Sources"
3. **Open the APK file** on phone
4. **Install** when prompted
5. **Launch the game** from app drawer

---

## ⚠️ Troubleshooting

### Build Fails?
- Make sure `buildozer.spec` is in the root directory
- Check the **Actions** tab for error logs
- Most common: Kivy version mismatch (already fixed in workflow)

### APK Won't Install?
- Might need API level adjustment in `buildozer.spec`
- Try lowering `android.api` from 31 to 28

### Need to Rebuild?
- Make changes to `main.py`
- Push to GitHub (automatically rebuilds)
- Or manually trigger in Actions tab

---

## Files in Your Repo:

✅ `main.py` - Kivy game code
✅ `buildozer.spec` - APK build config
✅ `.github/workflows/build.yml` - GitHub Actions workflow (AUTO-CREATED)

---

## 🎮 Done!
Your game is being built to APK on GitHub's servers right now!

**Next time you want to update:**
1. Edit `main.py` 
2. Push to GitHub
3. APK auto-rebuilds

---

Questions? Check the **Actions** tab logs for detailed error messages!
