# Changelog

All notable changes to DUP will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-19

### Added
- Initial release of DUP (Drive Upload Program)
- Authentication with Google Drive via OAuth 2.0
- `dup login` - Authenticate with Google Drive
- `dup ls` - List files in current or specified folder
- `dup tree` - Show recursive folder structure
- `dup cd` - Change current Drive folder
- `dup pwd` - Show current Drive path
- `dup up` - Upload files or folders with progress tracking
- `dup link` - Generate shareable links with privacy controls
- Cross-platform support (Windows & Linux)
- Windows installer with automatic PATH configuration
- Linux installation script
- Rich terminal UI with colors and tables
- Configuration persistence across sessions
- Token storage with automatic refresh
- Comprehensive documentation (README, QUICKSTART, DEVELOPER, SETUP)

### Security
- OAuth 2.0 authentication flow
- Local token storage
- Privacy-aware link sharing (asks before making files public)

### Platform Support
- Windows 10/11 with .exe installer
- Linux with pip installation
- Configuration directories:
  - Windows: %APPDATA%\dup\
  - Linux: ~/.config/dup/

## [Unreleased]

### Planned
- `dup down` - Download files from Drive
- `dup rm` - Delete files
- `dup mv` - Move/rename files
- `dup cp` - Copy files
- Folder synchronization
- File encryption before upload
- Interactive shell mode
- Search functionality
- Trash management
- Shared drive support
- Multiple account support

---

## Release Notes

### v1.0.0
This is the first stable release of DUP. It provides core functionality for navigating and uploading files to Google Drive through a simple command-line interface.

**Key Features:**
- Zero setup for end users (no Google Cloud project needed)
- Filesystem-like navigation (cd, ls, pwd)
- Easy file/folder uploads with progress bars
- Shareable link generation
- Beautiful terminal UI

**Installation:**
- Windows: Download and run the installer
- Linux: Clone repo and run install script

**Getting Started:**
```bash
dup login          # Authenticate
dup ls             # List files
dup cd Documents   # Navigate
dup up file.pdf    # Upload
dup link file.pdf  # Get link
```

See README.md for full documentation.
