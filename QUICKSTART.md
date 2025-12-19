# DUP - Quick Start Guide

## First Time Setup

### 1. Install DUP

**Windows:**
- Download and run the installer
- Open a new terminal

**Linux:**
```bash
git clone https://github.com/yourusername/dup.git
cd dup
./install-linux.sh
```

### 2. Authenticate

```bash
dup login
```

This will:
- Open your browser
- Ask you to sign in to Google
- Request permission to access your Drive
- Save your credentials locally

### 3. Start Using

```bash
# List your Drive files
dup ls

# Navigate to a folder
dup cd Documents

# Show current location
dup pwd

# Upload a file
dup up myfile.pdf

# Get a shareable link
dup link myfile.pdf
```

## Common Workflows

### Upload and Share a File

```bash
# Navigate to desired folder
dup cd "My Folder"

# Upload file
dup up document.pdf

# Get shareable link
dup link document.pdf
```

### Organize Files

```bash
# View current files
dup ls

# Navigate to organize
dup cd Projects

# Check structure
dup tree

# Go back
dup cd ..
```

### Upload Multiple Files

```bash
# Upload entire folder
dup up ./my-project

# Or upload files one by one
dup up file1.pdf
dup up file2.docx
dup up file3.xlsx
```

## Tips

- Use `dup tree` to visualize folder structure
- Use `dup pwd` when lost
- Paths can be absolute (`/Documents/Projects`) or relative (`../Documents`)
- File names with spaces need quotes: `dup up "my file.pdf"`
- `dup cd /` takes you to root

## Need Help?

```bash
dup --help           # General help
dup ls --help        # Command-specific help
dup version          # Check version
```

## Configuration Files

Your tokens and settings are stored in:
- Windows: `%APPDATA%\dup\`
- Linux: `~/.config/dup/`

These files are preserved even if you uninstall DUP.
