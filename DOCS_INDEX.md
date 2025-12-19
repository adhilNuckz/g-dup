# 📚 DUP Documentation Index

Welcome to DUP (Drive Upload Program)! This index helps you find the right documentation for your needs.

## 🚀 Quick Navigation

### I'm a New User
**Start here:** [START_HERE.md](START_HERE.md) → [QUICKSTART.md](QUICKSTART.md)

### I Want to Use DUP
**Read:** [README.md](README.md) for complete user guide

### I'm a Developer
**Start here:** [SETUP.md](SETUP.md) → [DEVELOPER.md](DEVELOPER.md)

### I Want to Contribute
**Read:** [CONTRIBUTING.md](CONTRIBUTING.md)

### I Want to Understand the Architecture
**Read:** [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)

---

## 📖 Complete Documentation List

### 🎯 Getting Started

#### [START_HERE.md](START_HERE.md)
**Purpose:** First document to read - tells you everything that's been created and how to get started.

**Read this if:**
- You just received this project
- You want a quick overview
- You need to know what to do next

**Contents:**
- Project contents checklist
- Quick start steps
- Building instructions
- Key features overview

---

#### [QUICKSTART.md](QUICKSTART.md)
**Purpose:** Fast-track guide to using DUP in 5 minutes.

**Read this if:**
- You want to start using DUP quickly
- You need basic usage examples
- You want common workflows

**Contents:**
- First time setup
- Common workflows
- Quick tips
- Basic commands

---

### 📚 User Documentation

#### [README.md](README.md)
**Purpose:** Complete user documentation and main project description.

**Read this if:**
- You want comprehensive user guide
- You need installation instructions
- You want detailed command reference
- You need troubleshooting help

**Contents:**
- Features overview
- Installation (Windows & Linux)
- All commands with examples
- Configuration details
- Building from source
- FAQ and troubleshooting
- Roadmap

---

#### [VISUAL_GUIDE.md](VISUAL_GUIDE.md)
**Purpose:** Visual reference with examples, diagrams, and UI previews.

**Read this if:**
- You learn better with visuals
- You want to see command output examples
- You need architecture diagrams
- You want a quick command cheat sheet

**Contents:**
- UI examples
- Flow diagrams
- Architecture visualization
- Command cheat sheet
- Workflow examples
- Color coding guide

---

### 🔧 Developer Documentation

#### [SETUP.md](SETUP.md)
**Purpose:** Step-by-step guide to get OAuth credentials and set up development environment.

**Read this if:**
- You're setting up DUP for development
- You need to get Google OAuth credentials
- You're preparing for distribution

**Contents:**
- Google Cloud Console setup
- OAuth credential creation
- Development installation
- Testing instructions
- Production preparation
- Troubleshooting

---

#### [DEVELOPER.md](DEVELOPER.md)
**Purpose:** Comprehensive developer guide for working on DUP.

**Read this if:**
- You're developing features
- You want to understand the codebase
- You need build instructions
- You want to know coding standards

**Contents:**
- Development environment setup
- Code structure explanation
- Adding new commands
- Testing procedures
- Building executables
- Distribution checklist
- Code style guidelines
- Resources and references

---

#### [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
**Purpose:** High-level architecture and design documentation.

**Read this if:**
- You want to understand the architecture
- You need to see how components interact
- You're planning major changes
- You want technical details

**Contents:**
- Project structure
- Architecture layers
- Data flow diagrams
- Technology stack
- State management
- Security model
- Development workflow
- Future roadmap

---

### 🤝 Contributing

#### [CONTRIBUTING.md](CONTRIBUTING.md)
**Purpose:** Guide for contributing to DUP.

**Read this if:**
- You want to contribute code
- You want to report bugs
- You want to suggest features
- You need PR guidelines

**Contents:**
- How to contribute
- Bug reporting template
- Feature request template
- Coding guidelines
- Commit message format
- Pull request process
- Code of conduct

---

### 📝 Project Information

#### [CHANGELOG.md](CHANGELOG.md)
**Purpose:** Version history and release notes.

**Read this if:**
- You want to know what's new
- You need version history
- You're planning upgrades

**Contents:**
- Version history
- Release notes
- Breaking changes
- New features
- Bug fixes

---

#### [LICENSE](LICENSE)
**Purpose:** MIT License - legal terms.

**Read this if:**
- You need to know licensing terms
- You're distributing DUP
- You have legal questions

---

### 🛠️ Development Tools

#### [dev.bat](dev.bat) (Windows)
**Purpose:** Helper script for Windows development tasks.

**Use this to:**
- Install in dev mode: `dev.bat install`
- Build executable: `dev.bat build`
- Run tests: `dev.bat test`
- Clean build files: `dev.bat clean`
- Run DUP: `dev.bat run login`

---

#### [dev.sh](dev.sh) (Linux)
**Purpose:** Helper script for Linux development tasks.

**Use this to:**
- Install in dev mode: `./dev.sh install`
- Build binary: `./dev.sh build`
- Run tests: `./dev.sh test`
- Clean build files: `./dev.sh clean`
- Run DUP: `./dev.sh run login`

---

### 📦 Configuration Files

#### [pyproject.toml](pyproject.toml)
**Purpose:** Python project configuration and dependencies.

**Contains:**
- Package metadata
- Dependencies
- Build system configuration
- Entry points
- Tool configurations

---

#### [requirements.txt](requirements.txt)
**Purpose:** Python dependencies list.

**Use this to:**
- Install dependencies: `pip install -r requirements.txt`

---

#### [.gitignore](.gitignore)
**Purpose:** Git ignore rules.

**Excludes:**
- Python cache files
- Build artifacts
- Credentials
- User tokens

---

### 🏗️ Build Scripts

#### [build_windows.py](build_windows.py)
**Purpose:** PyInstaller script to build Windows executable.

**Use:** `python build_windows.py`

**Output:** `dist/dup.exe`

---

#### [installer/windows.iss](installer/windows.iss)
**Purpose:** Inno Setup script for Windows installer.

**Use:** Compile with Inno Setup

**Output:** `dist/dup-setup-1.0.0.exe`

---

#### [install-linux.sh](install-linux.sh)
**Purpose:** Linux installation script.

**Use:** `./install-linux.sh`

---

## 🎯 Documentation by Use Case

### "I just want to use DUP"
1. [START_HERE.md](START_HERE.md) - Get overview
2. [SETUP.md](SETUP.md) - Get OAuth credentials
3. [QUICKSTART.md](QUICKSTART.md) - Start using it
4. [README.md](README.md) - Reference when needed

---

### "I want to develop DUP"
1. [START_HERE.md](START_HERE.md) - Understand what exists
2. [SETUP.md](SETUP.md) - Set up dev environment
3. [DEVELOPER.md](DEVELOPER.md) - Learn development workflow
4. [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) - Understand architecture
5. [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

### "I want to distribute DUP"
1. [DEVELOPER.md](DEVELOPER.md) - Build instructions
2. [SETUP.md](SETUP.md) - OAuth for production
3. [README.md](README.md) - User documentation to share
4. Build using `build_windows.py` or `dev.sh build`
5. Create installer with `windows.iss`

---

### "I want to contribute"
1. [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution process
2. [DEVELOPER.md](DEVELOPER.md) - Development setup
3. [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) - Architecture
4. Make changes
5. Submit PR

---

### "I'm stuck/confused"
1. [VISUAL_GUIDE.md](VISUAL_GUIDE.md) - See examples
2. [README.md](README.md) - Check FAQ
3. [SETUP.md](SETUP.md) - OAuth troubleshooting
4. [DEVELOPER.md](DEVELOPER.md) - Dev troubleshooting

---

## 📊 Documentation Map

```
Documentation Structure:

Getting Started
├── START_HERE.md          ⭐ Start here!
├── QUICKSTART.md          Quick tutorial
└── VISUAL_GUIDE.md        Visual examples

User Documentation
└── README.md              Complete guide

Developer Documentation
├── SETUP.md               OAuth setup
├── DEVELOPER.md           Dev guide
└── PROJECT_OVERVIEW.md    Architecture

Contributing
└── CONTRIBUTING.md        How to contribute

Project Info
├── CHANGELOG.md           Version history
└── LICENSE                MIT License

Development Tools
├── dev.bat                Windows helper
├── dev.sh                 Linux helper
├── build_windows.py       Windows build
└── install-linux.sh       Linux install

Configuration
├── pyproject.toml         Package config
├── requirements.txt       Dependencies
└── .gitignore            Git excludes

Installer
└── installer/
    └── windows.iss        Windows installer
```

---

## 🔍 Search by Topic

### Authentication
- [SETUP.md](SETUP.md) - OAuth setup
- [README.md](README.md) - User authentication
- [DEVELOPER.md](DEVELOPER.md) - Auth for production

### Commands
- [README.md](README.md) - Complete command reference
- [QUICKSTART.md](QUICKSTART.md) - Common commands
- [VISUAL_GUIDE.md](VISUAL_GUIDE.md) - Command examples

### Installation
- [README.md](README.md) - User installation
- [START_HERE.md](START_HERE.md) - Dev installation
- [SETUP.md](SETUP.md) - OAuth credentials

### Building
- [DEVELOPER.md](DEVELOPER.md) - Build process
- [START_HERE.md](START_HERE.md) - Quick build steps
- `build_windows.py` - Windows build script

### Contributing
- [CONTRIBUTING.md](CONTRIBUTING.md) - Main guide
- [DEVELOPER.md](DEVELOPER.md) - Code guidelines
- [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) - Architecture

### Troubleshooting
- [README.md](README.md) - User troubleshooting
- [SETUP.md](SETUP.md) - OAuth issues
- [DEVELOPER.md](DEVELOPER.md) - Dev issues

---

## 📱 Quick Reference

### File Sizes
- **Comprehensive**: README.md, DEVELOPER.md, PROJECT_OVERVIEW.md
- **Quick**: QUICKSTART.md, START_HERE.md
- **Visual**: VISUAL_GUIDE.md
- **Specific**: SETUP.md, CONTRIBUTING.md

### Time to Read
- **5 minutes**: START_HERE.md, QUICKSTART.md
- **15 minutes**: SETUP.md, VISUAL_GUIDE.md
- **30 minutes**: README.md, CONTRIBUTING.md
- **45 minutes**: DEVELOPER.md, PROJECT_OVERVIEW.md

---

## 🎓 Learning Paths

### New User Path
1. START_HERE.md (5 min)
2. SETUP.md (15 min - get credentials)
3. QUICKSTART.md (5 min)
4. Use DUP!
5. README.md (reference as needed)

### Developer Path
1. START_HERE.md (5 min)
2. SETUP.md (15 min)
3. DEVELOPER.md (45 min)
4. PROJECT_OVERVIEW.md (45 min)
5. Start developing!

### Contributor Path
1. START_HERE.md (5 min)
2. CONTRIBUTING.md (30 min)
3. DEVELOPER.md (45 min)
4. Make changes
5. Submit PR

---

## ❓ Still Can't Find What You Need?

1. **Search all docs**: Use Ctrl+F in your editor
2. **Check examples**: [VISUAL_GUIDE.md](VISUAL_GUIDE.md)
3. **Read FAQ**: [README.md](README.md#faq)
4. **Open an issue**: Report missing documentation

---

## 📝 Documentation Checklist

Before you start, make sure you have:

- [ ] Read [START_HERE.md](START_HERE.md)
- [ ] Obtained OAuth credentials (see [SETUP.md](SETUP.md))
- [ ] Installed dependencies
- [ ] Read relevant documentation for your use case

---

**Remember:** Documentation is organized by use case, not by file type. Start with your goal, then follow the recommended path!

**Happy reading! 📚**
