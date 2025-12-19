#!/usr/bin/env python3
"""
gdup build script for Linux
Creates standalone executable using PyInstaller
"""

from PyInstaller.__main__ import run
import os
import shutil
import sys

def main():
    print("="*60)
    print("Building gdup for Linux")
    print("="*60)
    
    # Clean previous builds
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    # PyInstaller options
    opts = [
        'dup/__main__.py',           # Entry point
        '--name=gdup',                # Executable name
        '--onefile',                  # Single executable
        '--console',                  # Console application
        '--clean',                    # Clean cache
        '--noconfirm',                # Don't ask for confirmation
        # Include credentials.json
        '--add-data=dup/credentials.json:dup',
        # Add hidden imports
        '--hidden-import=dup.cli',
        '--hidden-import=dup.auth',
        '--hidden-import=dup.drive',
        '--hidden-import=dup.config',
        '--hidden-import=dup.commands',
        '--hidden-import=googleapiclient.discovery',
        '--hidden-import=google.oauth2.credentials',
        '--hidden-import=google_auth_oauthlib.flow',
    ]
    
    print("\nRunning PyInstaller...")
    run(opts)
    
    print("\n" + "="*60)
    print("Build complete!")
    print("Executable: dist/gdup")
    print("\nTo test: ./dist/gdup --version")
    print("="*60)

if __name__ == "__main__":
    main()
