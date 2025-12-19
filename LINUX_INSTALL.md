# gdup Linux Installation Guide

## Available Installation Methods

### 1. .deb Package (Recommended for Debian/Ubuntu)

**For Debian, Ubuntu, Linux Mint, Pop!_OS, etc.**

```bash
# Download the .deb file
wget https://github.com/adhilNuckz/g-dup/releases/download/v1.0.0/gdup_1.0.0_amd64.deb

# Install
sudo dpkg -i gdup_1.0.0_amd64.deb

# If dependencies are missing, run:
sudo apt-get install -f

# Verify installation
gdup --version
```

**Uninstall:**
```bash
sudo dpkg -r gdup
```

### 2. Install Script (From Source)

```bash
# Clone repository
git clone https://github.com/adhilNuckz/g-dup.git
cd g-dup

# Run installer
chmod +x install-linux.sh
./install-linux.sh

# Add to PATH (if not already)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify
gdup --version
```

---

### 4. Binary Only

**Download pre-built binary:**

```bash
# Download
wget https://github.com/adhilNuckz/g-dup/releases/download/v1.0.0/gdup-linux

# Make executable
chmod +x gdup-linux

# Install system-wide
sudo mv gdup-linux /usr/local/bin/gdup

# Or install for current user only
mkdir -p ~/.local/bin
mv gdup-linux ~/.local/bin/gdup
export PATH="$HOME/.local/bin:$PATH"
```

---

## Quick Start

After installation:

```bash
# Authenticate with Google Drive
gdup login

# List files
gdup ls

# Upload a file
gdup up document.pdf

# Download a file
gdup down document.pdf

# Get help
gdup --help
```

---

## Building from Source

### Prerequisites

```bash
# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch Linux
sudo pacman -S python python-pip
```

### Build Binary

```bash
# Install PyInstaller
pip3 install pyinstaller

# Build
python3 build_linux.py

# Binary will be in dist/gdup
```

### Build .deb Package

```bash
# Install build tools
sudo apt-get install dpkg-dev

# Build binary first
python3 build_linux.py

# Build package
python3 build_deb.py

# Install
sudo dpkg -i dist/gdup_1.0.0_amd64.deb
```

### Build AppImage

```bash
# Build binary first
python3 build_linux.py

# Build AppImage (downloads appimagetool automatically)
python3 build_appimage.py

# Run
./dist/gdup-1.0.0-x86_64.AppImage
```

### Build All Formats

```bash
# Make executable
chmod +x build_linux_release.sh

# Run
./build_linux_release.sh

# Select option 4 for all formats
```

---

## Troubleshooting

### Command not found

Add to PATH:
```bash
# For ~/.local/bin
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# For /usr/local/bin
sudo cp gdup /usr/local/bin/
```

### Permission denied

Make executable:
```bash
chmod +x gdup
# or
chmod +x gdup-1.0.0-x86_64.AppImage
```

### SSL errors

The tool automatically retries failed connections. Check your internet connection.

### Authentication issues

You need to be added as a test user in Google Cloud Console OAuth consent screen.

---

## System Requirements

- **OS**: Linux (any distribution)
- **Architecture**: x86_64 (64-bit)
- **Python**: 3.8+ (for source installation)
- **Internet**: Required for Google Drive access

---

## Distribution-Specific Notes

### Ubuntu/Debian/Mint
Use the .deb package for easiest installation.

### Fedora/RHEL/CentOS
Use AppImage or binary installation.

### Arch Linux
Use AppImage or install from AUR (coming soon).

### Other Distributions
AppImage works on all distributions without modification.

---

## Uninstallation

### .deb package:
```bash
sudo dpkg -r gdup
```

### pip installation:
```bash
pip3 uninstall gdup
```

### Binary/AppImage:
```bash
# Just delete the file
rm /usr/local/bin/gdup
# or
rm ~/.local/bin/gdup
```

---

## Getting Help

- **Documentation**: https://gdup.dev/docs
- **Issues**: https://github.com/adhilNuckz/g-dup/issues
- **Email**: contact@gdup.com
