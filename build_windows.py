# DUP build script for Windows
# Creates standalone executable using PyInstaller

from PyInstaller.__main__ import run
import os
import shutil

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
    '--icon=NONE',                # Add icon later if needed
    '--clean',                    # Clean cache
    '--noconfirm',                # Don't ask for confirmation
    # Include credentials.json
    '--add-data=dup/credentials.json;dup',
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

# Run PyInstaller
run(opts)

print("\n" + "="*60)
print("Build complete!")
print("Executable: dist/gdup.exe")
print("="*60)
