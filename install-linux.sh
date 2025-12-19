#!/bin/bash
# DUP Installation Script for Linux

set -e

echo "=========================================="
echo "Installing DUP - Drive Upload Program"
echo "=========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Found Python $PYTHON_VERSION"

# Install using pip
echo ""
echo "Installing DUP..."

if command -v pip3 &> /dev/null; then
    pip3 install --user .
elif command -v pip &> /dev/null; then
    pip install --user .
else
    echo "Error: pip is not installed."
    echo "Please install pip and try again."
    exit 1
fi

echo ""
echo "=========================================="
echo "Installation complete!"
echo ""
echo "DUP has been installed to your user directory."
echo ""
echo "To use DUP, make sure ~/.local/bin is in your PATH:"
echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
echo ""
echo "Add this line to your ~/.bashrc or ~/.zshrc to make it permanent."
echo ""
echo "Then run: dup login"
echo "=========================================="
