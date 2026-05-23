#!/bin/bash
# WSL Setup Script for Dots and Boxes APK Build

echo "=== Setting up build environment in WSL ==="

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    openjdk-11-jdk \
    android-sdk

# Install Python build tools
pip3 install --upgrade setuptools wheel pip cython

# Install buildozer
pip3 install buildozer

echo "=== Build environment ready ==="
echo "Next steps:"
echo "1. Copy SanskarDE folder to /mnt/c/SanskarDE"
echo "2. cd /mnt/c/SanskarDE"
echo "3. buildozer android debug"
echo "4. APK will be in: bin/"
