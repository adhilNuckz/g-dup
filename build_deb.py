#!/usr/bin/env python3
"""
Create .deb package for gdup
Requires: dist/gdup binary (run build_linux.py first)
"""

import os
import shutil
import subprocess
import sys

VERSION = "1.0.0"
PACKAGE_NAME = "gdup"
ARCH = "amd64"  # or "arm64" for ARM

def create_deb_structure():
    """Create Debian package directory structure"""
    
    # Base directory
    deb_dir = f"{PACKAGE_NAME}_{VERSION}_{ARCH}"
    
    # Clean existing
    if os.path.exists(deb_dir):
        shutil.rmtree(deb_dir)
    
    # Create structure
    dirs = [
        f"{deb_dir}/DEBIAN",
        f"{deb_dir}/usr/local/bin",
        f"{deb_dir}/usr/share/doc/{PACKAGE_NAME}",
        f"{deb_dir}/usr/share/applications",
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    
    return deb_dir

def create_control_file(deb_dir):
    """Create DEBIAN/control file"""
    control_content = f"""Package: {PACKAGE_NAME}
Version: {VERSION}
Section: utils
Priority: optional
Architecture: {ARCH}
Maintainer: DND <contact@gdup.com>
Description: Google Drive Upload Program
 A powerful CLI tool for managing Google Drive files from the terminal.
 Features include upload, download, file listing, folder navigation,
 and shareable link generation.
Homepage: https://github.com/adhilNuckz/g-dup
"""
    
    with open(f"{deb_dir}/DEBIAN/control", 'w') as f:
        f.write(control_content)

def create_postinst_script(deb_dir):
    """Create post-installation script"""
    postinst_content = """#!/bin/bash
set -e

# Make binary executable
chmod +x /usr/local/bin/gdup

echo "gdup has been installed successfully!"
echo "Run 'gdup login' to get started."

exit 0
"""
    
    postinst_path = f"{deb_dir}/DEBIAN/postinst"
    with open(postinst_path, 'w') as f:
        f.write(postinst_content)
    os.chmod(postinst_path, 0o755)

def copy_files(deb_dir):
    """Copy executable and documentation"""
    
    # Check if binary exists
    if not os.path.exists('dist/gdup'):
        print("Error: dist/gdup not found. Run build_linux.py first.")
        sys.exit(1)
    
    # Copy binary
    shutil.copy('dist/gdup', f"{deb_dir}/usr/local/bin/gdup")
    os.chmod(f"{deb_dir}/usr/local/bin/gdup", 0o755)
    
    # Copy documentation
    if os.path.exists('README.md'):
        shutil.copy('README.md', f"{deb_dir}/usr/share/doc/{PACKAGE_NAME}/README.md")
    
    if os.path.exists('LICENSE'):
        shutil.copy('LICENSE', f"{deb_dir}/usr/share/doc/{PACKAGE_NAME}/copyright")
    
    # Create changelog
    changelog_content = f"""{PACKAGE_NAME} ({VERSION}) stable; urgency=medium

  * Initial release
  * CLI tool for Google Drive management
  * Upload, download, and file operations
  * OAuth 2.0 authentication

 -- DND <contact@gdup.com>  {subprocess.check_output(['date', '-R']).decode().strip()}
"""
    
    changelog_path = f"{deb_dir}/usr/share/doc/{PACKAGE_NAME}/changelog.Debian"
    with open(changelog_path, 'w') as f:
        f.write(changelog_content)
    
    # Compress changelog
    subprocess.run(['gzip', '-9', changelog_path])

def build_deb_package(deb_dir):
    """Build the .deb package"""
    
    print(f"\nBuilding {deb_dir}.deb...")
    
    # Build package
    subprocess.run(['dpkg-deb', '--build', deb_dir])
    
    # Move to dist directory
    os.makedirs('dist', exist_ok=True)
    deb_file = f"{deb_dir}.deb"
    if os.path.exists(deb_file):
        shutil.move(deb_file, f"dist/{deb_file}")
        print(f"\n✓ Package created: dist/{deb_file}")
    
    # Clean up
    shutil.rmtree(deb_dir)

def main():
    print("="*60)
    print("Creating .deb package for gdup")
    print("="*60)
    
    # Check if dpkg-deb is available
    if shutil.which('dpkg-deb') is None:
        print("Error: dpkg-deb not found. Install it with:")
        print("  sudo apt-get install dpkg-dev")
        sys.exit(1)
    
    # Create package structure
    deb_dir = create_deb_structure()
    print(f"✓ Created package structure: {deb_dir}")
    
    # Create control files
    create_control_file(deb_dir)
    print("✓ Created control file")
    
    create_postinst_script(deb_dir)
    print("✓ Created post-install script")
    
    # Copy files
    copy_files(deb_dir)
    print("✓ Copied files")
    
    # Build package
    build_deb_package(deb_dir)
    
    print("\n" + "="*60)
    print("Package build complete!")
    print(f"Install with: sudo dpkg -i dist/{deb_dir}.deb")
    print("="*60)

if __name__ == "__main__":
    main()
