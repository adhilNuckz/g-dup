#!/bin/bash
# Master build script for gdup Linux releases

set -e

echo "=========================================="
echo "gdup Linux Release Builder"
echo "=========================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required"
    exit 1
fi

# Check PyInstaller
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "Installing PyInstaller..."
    pip3 install pyinstaller
fi

# Menu
echo "Select build type:"
echo "1) Binary only (PyInstaller)"
echo "2) .deb package (Debian/Ubuntu)"
echo "3) AppImage (Universal)"
echo "4) All formats"
echo ""
read -p "Choice [1-4]: " choice

case $choice in
    1)
        echo ""
        echo "Building binary..."
        python3 build_linux.py
        echo ""
        echo "✓ Binary created: dist/gdup"
        ;;
    2)
        echo ""
        echo "Building binary..."
        python3 build_linux.py
        echo ""
        echo "Building .deb package..."
        python3 build_deb.py
        ;;
    3)
        echo ""
        echo "Building binary..."
        python3 build_linux.py
        echo ""
        echo "Building AppImage..."
        python3 build_appimage.py
        ;;
    4)
        echo ""
        echo "Building binary..."
        python3 build_linux.py
        echo ""
        echo "Building .deb package..."
        python3 build_deb.py
        echo ""
        echo "Building AppImage..."
        python3 build_appimage.py
        echo ""
        echo "=========================================="
        echo "All builds complete!"
        echo "=========================================="
        ls -lh dist/
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "Build complete! Check dist/ directory"
