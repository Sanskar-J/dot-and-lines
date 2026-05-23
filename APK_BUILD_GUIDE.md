# Dots and Boxes - APK Build Instructions

## What's Been Created:
1. **main.py** - Kivy version of the Dots and Boxes game (mobile-compatible)
2. **buildozer.spec** - Configuration file for APK building

## Prerequisites for APK Building:

Buildozer **only works on Linux** (Ubuntu, Debian). You have three options:

### Option 1: Use Windows Subsystem for Linux (WSL) - EASIEST
```bash
# 1. Install WSL2 with Ubuntu (Windows Powershell as Admin):
wsl --install

# 2. Open Ubuntu terminal and run:
cd /mnt/c/SanskarDE
sudo apt-get update
sudo apt-get install -y python3-pip git
pip3 install buildozer cython

# 3. Build APK:
buildozer android debug

# APK will be in: bin/dotsandboxes-0.1-debug.apk
```

### Option 2: Use Online Builder
1. Visit: https://buildozer.kivy.org/
2. Upload the `buildozer.spec` and `main.py` files
3. Click "Build" - they'll compile to APK on their Linux server

### Option 3: Use Docker (if you have Docker installed)
```bash
docker run -v c:/SanskarDE:/home/user/project kivy/kivy:latest buildozer android debug
```

## Files Created:
- `main.py` - Kivy app source code
- `buildozer.spec` - APK build configuration

## Game Features:
- 2-player dots and boxes game
- Blue and Red player colors
- Tap between dots to draw lines
- Complete a box to score and get another turn
- Mobile-responsive UI

## To Test on Windows (Without APK):
```bash
cd c:\SanskarDE
python main.py  # (after Kivy installs successfully)
```

**Note:** Kivy on Python 3.14 has missing dependencies. Use Python 3.11 or 3.12 for best results.
