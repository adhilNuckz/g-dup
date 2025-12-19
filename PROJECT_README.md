# 🎉 DUP - Drive Upload Program

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/dup)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/dup)

> A cross-platform CLI tool for managing Google Drive files with a filesystem-like interface.

```bash
dup login              # Authenticate once
dup ls                 # List your Drive files
dup cd Documents       # Navigate folders
dup up myfile.pdf      # Upload with progress
dup link myfile.pdf    # Get shareable link
```

---

## ⚡ Quick Start

### For End Users

**🪟 Windows**
```bash
# Download installer from Releases
# Run dup-setup-1.0.0.exe
# Open new terminal and run:
dup login
```

**🐧 Linux**
```bash
git clone https://github.com/yourusername/dup.git
cd dup
./install-linux.sh
dup login
```

### For Developers

```bash
git clone https://github.com/yourusername/dup.git
cd dup
pip install -e .
# Get OAuth credentials (see SETUP.md)
dup login
```

---

## 🌟 Key Features

- **🔐 Zero Setup** - No Google Cloud project required for users
- **📁 Filesystem-like** - Familiar commands: `ls`, `cd`, `pwd`
- **⬆️ Easy Upload** - Files and folders with progress bars
- **🔗 Link Sharing** - Generate shareable links instantly
- **🎨 Beautiful UI** - Rich colors, tables, and progress indicators
- **🖥️ Cross-platform** - Windows and Linux support
- **⚡ Fast** - Lightweight and efficient
- **🔒 Secure** - OAuth 2.0 authentication

---

## 📚 Complete Documentation

| Document | Purpose | Read Time |
|----------|---------|-----------|
| **[START_HERE.md](START_HERE.md)** | 🚀 **Start here!** Project overview | 5 min |
| [README.md](README.md) | Complete user guide | 30 min |
| [QUICKSTART.md](QUICKSTART.md) | 5-minute tutorial | 5 min |
| [SETUP.md](SETUP.md) | OAuth setup for developers | 15 min |
| [DEVELOPER.md](DEVELOPER.md) | Development guide | 45 min |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute | 30 min |
| [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) | Architecture details | 45 min |
| [VISUAL_GUIDE.md](VISUAL_GUIDE.md) | Examples and diagrams | 15 min |
| [DOCS_INDEX.md](DOCS_INDEX.md) | Documentation navigation | 5 min |
| [PROJECT_COMPLETE.md](PROJECT_COMPLETE.md) | Project summary | 10 min |

**📖 New to DUP?** Start with [START_HERE.md](START_HERE.md)

---

## 🎯 Features in Detail

### Commands

| Command | Description | Example |
|---------|-------------|---------|
| `login` | Authenticate with Google Drive | `dup login` |
| `ls` | List files in current/specified folder | `dup ls Documents` |
| `tree` | Show recursive folder structure | `dup tree` |
| `cd` | Change current Drive folder | `dup cd Projects` |
| `pwd` | Show current Drive path | `dup pwd` |
| `up` | Upload file or folder | `dup up myfile.pdf` |
| `link` | Generate shareable link | `dup link myfile.pdf` |
| `version` | Show version information | `dup version` |

### User Experience

**Beautiful Tables**
```
📂 /Documents

Type    Name              Size      Modified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 DIR  Projects          -         2025-01-15
📄 FILE report.pdf        2.3 MB    2025-01-14

2 items
```

**Progress Bars**
```
Uploading myfile.pdf
████████████████████ 100% 0:00:03

✓ Uploaded: myfile.pdf
```

**Privacy Controls**
```
⚠️  File 'report.pdf' is private.
Make it publicly accessible? [y/n]:
```

---

## 🏗️ Project Structure

```
dup/
├── 📂 dup/                      # Main package
│   ├── cli.py                   # CLI application
│   ├── auth.py                  # OAuth authentication
│   ├── drive.py                 # Drive API helpers
│   ├── config.py                # Configuration management
│   └── 📂 commands/             # All commands
│       ├── ls.py               # List files
│       ├── tree.py             # Tree view
│       ├── cd.py               # Change directory
│       ├── pwd.py              # Print working directory
│       ├── upload.py           # Upload files
│       └── link.py             # Generate links
│
├── 📂 installer/                # Build scripts
│   └── windows.iss             # Windows installer
│
├── 📄 pyproject.toml            # Package configuration
├── 📄 requirements.txt          # Dependencies
├── 📄 build_windows.py          # Windows build script
├── 📄 install-linux.sh          # Linux install script
├── 📄 dev.bat                   # Windows dev helper
├── 📄 dev.sh                    # Linux dev helper
│
└── 📚 Documentation/            # Complete docs
    ├── README.md               # User guide
    ├── START_HERE.md           # Getting started
    ├── QUICKSTART.md           # Quick tutorial
    ├── SETUP.md                # OAuth setup
    ├── DEVELOPER.md            # Dev guide
    ├── CONTRIBUTING.md         # Contribution guide
    ├── PROJECT_OVERVIEW.md     # Architecture
    ├── VISUAL_GUIDE.md         # Visual examples
    ├── DOCS_INDEX.md           # Doc navigation
    ├── PROJECT_COMPLETE.md     # Project summary
    └── CHANGELOG.md            # Version history
```

---

## 🚀 Development

### Prerequisites
- Python 3.8 or higher
- pip
- Google OAuth credentials (see [SETUP.md](SETUP.md))

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/dup.git
cd dup

# Install in development mode
pip install -e .

# Or use helper scripts
# Windows: dev.bat install
# Linux: ./dev.sh install
```

### Quick Commands

**Windows:**
```bash
dev.bat install    # Install in dev mode
dev.bat build      # Build executable
dev.bat test       # Run tests
dev.bat clean      # Clean build files
dev.bat run ls     # Run DUP
```

**Linux:**
```bash
./dev.sh install   # Install in dev mode
./dev.sh build     # Build binary
./dev.sh test      # Run tests
./dev.sh clean     # Clean build files
./dev.sh run ls    # Run DUP
```

---

## 🔐 OAuth Setup (Developers)

To develop or distribute DUP, you need Google OAuth credentials:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google Drive API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download `credentials.json`
6. Place in `dup/` directory

**Detailed instructions:** [SETUP.md](SETUP.md)

---

## 📦 Building for Distribution

### Windows

```bash
# Build executable
python build_windows.py
# Creates: dist/dup.exe

# Create installer (requires Inno Setup)
# Open installer/windows.iss in Inno Setup
# Click "Compile"
# Creates: dist/dup-setup-1.0.0.exe
```

### Linux

```bash
# Install from source
./install-linux.sh

# Or build binary
pip install pyinstaller
pyinstaller --onefile dup/__main__.py --name dup
# Creates: dist/dup
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report bugs
- How to suggest features
- Code style guidelines
- Pull request process

### Quick Contribution Guide

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Commit: `git commit -m 'feat: add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

---

## 🐛 Troubleshooting

**"Not authenticated with Google Drive"**
```bash
Solution: Run `dup login`
```

**"credentials.json not found" (Developers)**
```bash
Solution: Get OAuth credentials from Google Cloud Console
See SETUP.md for instructions
```

**PATH not found after installation**
```bash
# Windows: Restart terminal or log out/in
# Linux: Add ~/.local/bin to PATH
export PATH="$HOME/.local/bin:$PATH"
```

**More help:** See [README.md](README.md#troubleshooting)

---

## 📋 Roadmap

### v1.0.0 (Current) ✅
- OAuth authentication
- File navigation (ls, cd, pwd, tree)
- File upload
- Link generation
- Cross-platform support
- Windows & Linux installers

### v2.0.0 (Planned)
- [ ] Download files (`dup down`)
- [ ] Delete files (`dup rm`)
- [ ] Move/rename (`dup mv`)
- [ ] Copy files (`dup cp`)
- [ ] Search functionality

### v3.0.0 (Future)
- [ ] Folder synchronization
- [ ] File encryption
- [ ] Interactive shell mode
- [ ] Shared drives support
- [ ] Multiple accounts

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📊 Stats

- **Version:** 1.0.0
- **Python:** 3.8+
- **Lines of Code:** ~1,500+
- **Documentation:** 10,000+ words
- **Commands:** 7
- **Status:** Production Ready

---

## 🙏 Acknowledgments

- Google Drive API
- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal UI
- [PyInstaller](https://pyinstaller.org/) - Executable creation
- [Inno Setup](https://jrsoftware.org/isinfo.php) - Windows installer

---

## 📧 Support

- **Documentation:** See [DOCS_INDEX.md](DOCS_INDEX.md)
- **Issues:** [GitHub Issues](https://github.com/yourusername/dup/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/dup/discussions)

---

## ⭐ Star Us!

If you find DUP useful, please give it a star on GitHub!

---

<p align="center">
  <strong>Made with ❤️ for easier Google Drive management</strong>
</p>

<p align="center">
  <a href="START_HERE.md">Getting Started</a> •
  <a href="README.md">User Guide</a> •
  <a href="DEVELOPER.md">Developer Guide</a> •
  <a href="CONTRIBUTING.md">Contributing</a>
</p>
