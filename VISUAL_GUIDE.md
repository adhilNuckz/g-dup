# DUP - Visual Reference Guide

## 🎨 User Interface Examples

### Command: `dup ls`

```
📂 /Documents/Projects

Type    Name              Size      Modified
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📁 DIR  Code              -         2025-01-15
📁 DIR  Images            -         2025-01-14
📄 FILE report.pdf        2.3 MB    2025-01-13
📄 FILE notes.txt         15.2 KB   2025-01-12
📄 FILE data.xlsx         856.0 KB  2025-01-11

5 items
```

### Command: `dup tree`

```
📂 /Documents
├── 📁 Projects
│   ├── 📄 README.md
│   ├── 📁 src
│   │   ├── 📄 main.py
│   │   ├── 📄 utils.py
│   │   └── 📁 tests
│   │       └── 📄 test_main.py
│   └── 📄 requirements.txt
├── 📄 report.pdf
└── 📁 Images
    ├── 📄 photo1.jpg
    └── 📄 photo2.jpg
```

### Command: `dup up myfile.pdf`

```
Uploading myfile.pdf
████████████████████ 100% 0:00:03

✓ Uploaded: myfile.pdf
Link: https://drive.google.com/file/d/1a2b3c4d5e/view
```

### Command: `dup link myfile.pdf`

```
⚠️  File 'myfile.pdf' is private.
Make it publicly accessible? [y/n]: y

✓ File is now public
📎 Link: https://drive.google.com/file/d/1a2b3c4d5e/view
```

## 🗺️ Command Flow Diagrams

### Authentication Flow

```
┌─────────────┐
│ dup login   │
└──────┬──────┘
       │
       ▼
┌─────────────────┐     ┌────────────┐
│ Token exists?   ├─Yes─►Use token   │
└────┬────────────┘     └─────┬──────┘
     │No                      │
     ▼                        ▼
┌──────────────┐         ┌────────────┐
│ Open browser │         │ API ready! │
└──────┬───────┘         └────────────┘
       │
       ▼
┌───────────────┐
│ User signs in │
└──────┬────────┘
       │
       ▼
┌──────────────┐
│ Save token   │
└──────┬───────┘
       │
       ▼
┌────────────┐
│ Done!      │
└────────────┘
```

### File Upload Flow

```
┌─────────────────────┐
│ dup up myfile.pdf   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ File exists?        │
└──────┬──────────────┘
       │Yes
       ▼
┌─────────────────────┐
│ Get current folder  │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Start upload        │
│ Show progress bar   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Upload complete     │
│ Display link        │
└─────────────────────┘
```

### Navigation Flow

```
┌──────────────┐
│ dup cd path  │
└──────┬───────┘
       │
       ▼
┌─────────────────────┐
│ Resolve path        │
│ (handle .., /, etc) │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Folder exists?      │
└──────┬──────────────┘
       │Yes
       ▼
┌─────────────────────┐
│ Update state.json   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Show new path       │
└─────────────────────┘
```

## 📊 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        User Terminal                         │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     CLI Layer (cli.py)                       │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │  login   │    ls    │   tree   │    cd    │    up    │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                  Command Layer (commands/)                   │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │   ls.py  │ tree.py  │  cd.py   │  pwd.py  │upload.py │  │
│  │          │          │          │          │ link.py  │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
└────────────────────────────┬────────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   auth.py       │ │   drive.py      │ │   config.py     │
│                 │ │                 │ │                 │
│ OAuth flow      │ │ Drive API ops   │ │ State mgmt      │
│ Token mgmt      │ │ File ops        │ │ Config dirs     │
│ Service obj     │ │ Path resolution │ │ Persistence     │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│               Google Drive API (Google Cloud)                │
└─────────────────────────────────────────────────────────────┘
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  OAuth      │     │  Drive API  │     │ User's      │
│  Server     │     │  Endpoints  │     │ Drive Data  │
└─────────────┘     └─────────────┘     └─────────────┘
```

## 🗂️ File System Layout

### Configuration Directories

**Windows:**
```
C:\Users\YourName\AppData\Roaming\
└── dup\
    ├── token.json       # OAuth token
    └── state.json       # Current folder state
```

**Linux:**
```
~/.config/
└── dup/
    ├── token.json       # OAuth token
    └── state.json       # Current folder state
```

### Installation Directories

**Windows:**
```
C:\Program Files\
└── dup\
    └── dup.exe          # Main executable
```

**Linux:**
```
/usr/local/bin/
└── dup                  # Main executable

# Or for user install:
~/.local/bin/
└── dup                  # Main executable
```

## 🎯 Command Cheat Sheet

### Basic Navigation
```bash
dup login              # Authenticate
dup pwd                # Show current path
dup ls                 # List current folder
dup ls /               # List root
dup ls Documents       # List Documents folder
dup cd Documents       # Change to Documents
dup cd /               # Go to root
dup cd ..              # Go to parent
```

### Folder Visualization
```bash
dup tree               # Show tree from current folder
dup tree /             # Show tree from root
dup tree Documents     # Show tree from Documents
```

### File Operations
```bash
dup up file.pdf                  # Upload single file
dup up "my file.pdf"             # Upload file with spaces
dup up ./myfolder                # Upload entire folder
dup link file.pdf                # Get shareable link
```

### Path Examples
```bash
# Absolute paths (from root)
dup cd /Documents/Projects
dup ls /Photos/Vacation

# Relative paths (from current location)
dup cd Projects
dup cd ../Reports
dup cd ../../

# Special paths
dup cd .                # Stay in current folder
dup cd ..               # Go up one level
dup cd /                # Go to root
```

## 🎨 Color Coding

DUP uses colors to make output clearer:

- **🟢 Green**: Success messages, completed actions
- **🔴 Red**: Errors, failed operations
- **🟡 Yellow**: Warnings, confirmations needed
- **🔵 Cyan**: Information, paths, titles
- **⚪ Gray/Dim**: Secondary information, dates

## 📱 Status Indicators

- **✓** Success
- **⚠️** Warning
- **📁** Folder
- **📄** File
- **📎** Link
- **🔄** Progress/Loading

## 🔄 Workflow Examples

### Organize and Share Files

```bash
# 1. See what you have
dup ls

# 2. Navigate to target folder
dup cd "Project Files"

# 3. Check structure
dup tree

# 4. Upload new file
dup up report.pdf

# 5. Get shareable link
dup link report.pdf
```

### Upload Project Folder

```bash
# 1. Go to where you want it
dup cd Projects

# 2. Upload entire folder
dup up ./my-project

# 3. Verify it uploaded
dup tree
```

### Find and Share File

```bash
# 1. List root
dup ls /

# 2. Navigate to folder
dup cd Documents

# 3. List files
dup ls

# 4. Get link
dup link important-file.pdf
```

## 📐 Error Messages

### Common Errors and Solutions

**"Not authenticated with Google Drive"**
```bash
Solution: Run `dup login`
```

**"Path not found: Documents"**
```bash
Solution: Check spelling, or use `dup ls` to see available folders
```

**"File not found: myfile.pdf"**
```bash
Solution: Verify file name with `dup ls`, check current directory
```

**"credentials.json not found" (Developers)**
```bash
Solution: Get OAuth credentials from Google Cloud Console
          See SETUP.md for instructions
```

## 🎓 Learning Path

### Beginner
1. `dup login` - Authenticate
2. `dup ls` - List files
3. `dup pwd` - Check location
4. `dup cd` - Navigate

### Intermediate
5. `dup tree` - Visualize structure
6. `dup up` - Upload files
7. `dup link` - Share files

### Advanced
- Upload folders recursively
- Navigate with relative/absolute paths
- Organize Drive systematically

## 🔗 Quick Links in Documentation

- **Installation**: README.md
- **Quick Start**: QUICKSTART.md or START_HERE.md
- **Development**: DEVELOPER.md
- **OAuth Setup**: SETUP.md
- **Contributing**: CONTRIBUTING.md
- **Architecture**: PROJECT_OVERVIEW.md

---

**This is a complete visual reference for DUP!**

For actual usage, start with [START_HERE.md](START_HERE.md) or [README.md](README.md).
