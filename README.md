# gdup - Google Drive Upload Program

<p align="center">
  <strong>A cross-platform CLI tool for managing Google Drive files</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#commands">Commands</a> •
  <a href="#building">Building</a>
</p>

---

## 🎯 Features

- **Zero Setup**: No Google Cloud project required for end users
- **Filesystem-like Interface**: Navigate Drive with familiar commands (`ls`, `cd`, `pwd`)
- **Easy Upload**: Upload files and folders with progress tracking
- **Link Sharing**: Generate shareable links with privacy controls
- **Cross-platform**: Works on Windows and Linux
- **Beautiful UI**: Rich terminal interface with colors and tables

## 📦 Installation

### Windows

1. Download the installer from [Releases](https://github.com/yourusername/gdup/releases)
2. Run `gdup-setup-1.0.0.exe`
3. The installer will:
   - Install gdup to `C:\Program Files\gdup\`
   - Add gdup to your PATH automatically
   - Create an uninstaller entry in Apps & Features

After installation, open a new terminal and run:
```bash
gdup login
```

### Linux

#### Method 1: Install from source
```bash
git clone https://github.com/yourusername/gdup.git
cd gdup
chmod +x install-linux.sh
./install-linux.sh
```

#### Method 2: Using pip
```bash
git clone https://github.com/yourusername/gdup.git
cd gdup
pip install --user .
```

Make sure `~/.local/bin` is in your PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

Add this line to your `~/.bashrc` or `~/.zshrc` to make it permanent.

## 🚀 Usage

### First Time Setup

1. **Authenticate with Google Drive:**
   ```bash
   gdup login
   ```
   This will open your browser to authenticate with Google.

2. **List files in your Drive:**
   ```bash
   gdup ls
   ```

3. **Navigate folders:**
   ```bash
   gdup cd Documents
   gdup pwd
   ```

4. **Upload files:**
   ```bash
   gdup up myfile.pdf
   gdup up myfolder/
   ```

5. **Download files:**
   ```bash
   gdup down myfile.pdf
   ```

6. **Get shareable links:**
   ```bash
   gdup link myfile.pdf
   ```

## 📚 Commands

### `gdup login`
Authenticate with Google Drive.

**Example:**
```bash
gdup login
```

Opens your browser for OAuth authentication. Your credentials are saved locally and you won't need to login again unless the token expires.

---

### `gdup ls [path]`
List files in current or specified Drive folder.

**Examples:**
```bash
gdup ls              # List current folder
gdup ls Documents    # List Documents folder
gdup ls /            # List root folder
```

**Output:**
```
📂 /Documents

Type    Name              Size      Modified
📁 DIR  Projects          -         2025-01-15
📄 FILE report.pdf        2.3 MB    2025-01-14
📄 FILE notes.txt         15.2 KB   2025-01-13

3 items
```

---

### `gdup tree [path]`
Show recursive folder structure.

**Examples:**
```bash
gdup tree              # Tree from current folder
gdup tree Documents    # Tree from Documents folder
```

**Output:**
```
📂 /Documents
├── 📁 Projects
│   ├── 📄 project1.txt
│   └── 📁 Code
│       └── 📄 main.py
└── 📄 report.pdf
```

---

### `gdup cd <path>`
Change current Drive folder.

**Examples:**
```bash
gdup cd Documents        # Go to Documents
gdup cd ..               # Go to parent folder
gdup cd /                # Go to root
gdup cd Projects/Code    # Navigate multiple levels
```

---

### `gdup pwd`
Show current Drive path.

**Example:**
```bash
gdup pwd
```

**Output:**
```
/Documents/Projects
```

---

### `gdup up <path>`
Upload file or folder to current Drive location.

**Examples:**
```bash
gdup up report.pdf           # Upload a file
gdup up ./myfolder           # Upload a folder
gdup up "my document.docx"   # Upload file with spaces
```

**Output:**
```
Uploading report.pdf
████████████████████ 100% 0:00:00

✓ Uploaded: report.pdf
Link: https://drive.google.com/file/d/xxxxx/view
```

---

### `gdup link <filename>`
Generate shareable Google Drive link for a file.

**Examples:**
```bash
gdup link report.pdf
```

**Behavior:**
- If file is private, asks for confirmation to make public
- If file is already shared, shows link immediately
- Provides Google Drive web link

**Output:**
```
⚠️  File 'report.pdf' is private.
Make it publicly accessible? [y/n]: y

✓ File is now public
📎 Link: https://drive.google.com/file/d/xxxxx/view
```

---

### `gdup down <filename> [--dest <path>]`
Download a file from current Drive location to local machine.

**Examples:**
```bash
gdup down report.pdf                    # Download to current directory
gdup down report.pdf --dest ~/Downloads # Download to specific directory
gdup down report.pdf -d myfile.pdf      # Download with custom name
```

**Features:**
- Downloads with progress bar
- Supports Google Docs/Sheets/Slides (exports to PDF/Excel/PowerPoint)
- Preserves original filename by default

**Output:**
```
Downloading report.pdf
████████████████████ 100% 0:00:02

✓ Downloaded: report.pdf
Saved to: report.pdf
```

**Note:** Folder downloads are not yet supported. Use `gdup down` for individual files only.

---

### `gdup version`
Show version information.

**Example:**
```bash
gdup version
```

**Output:**
```
gdup version 1.0.0
```

## 🔧 Configuration

gdup stores configuration and tokens in platform-specific locations:

- **Windows**: `%APPDATA%\gdup\`
  - `token.json` - OAuth token
  - `state.json` - Current folder state

- **Linux**: `~/.config/gdup/`
  - `token.json` - OAuth token
  - `state.json` - Current folder state

### Uninstallation

**Windows:**
1. Go to Settings > Apps > Installed apps
2. Find "gdup" and click Uninstall
3. Your tokens and configuration are preserved in `%APPDATA%\gdup\`

**Linux:**
```bash
pip uninstall gdup
```

To remove configuration:
```bash
rm -rf ~/.config/gdup
```

## 🛠️ Building from Source

### Prerequisites

- Python 3.8 or higher
- pip
- PyInstaller (for building executables)
- Inno Setup (for Windows installer)

### Building for Windows

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install pyinstaller
   ```

2. **Build executable:**
   ```bash
   python build_windows.py
   ```
   This creates `dist/gdup.exe`

3. **Create installer (requires Inno Setup):**
   - Install [Inno Setup](https://jrsoftware.org/isinfo.php)
   - Open `installer/windows.iss` in Inno Setup
   - Click "Compile"
   - Installer will be created in `dist/`

### Building for Linux

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build and install:**
   ```bash
   pip install --user .
   ```

3. **Or create a standalone binary:**
   ```bash
   pyinstaller --onefile gdup/__main__.py --name gdup
   ```
   Copy `dist/gdup` to `/usr/local/bin/`

## 🔐 OAuth Credentials Setup (For Developers)

To distribute gdup, you need to embed OAuth credentials. Here's how:

1. **Create a Google Cloud Project:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project

2. **Enable Google Drive API:**
   - In the project, go to "APIs & Services" > "Library"
   - Search for "Google Drive API"
   - Click "Enable"

3. **Create OAuth 2.0 Credentials:**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop app"
   - Download the credentials JSON file

4. **Add Credentials to gdup:**
   - Place `credentials.json` in the `gdup/` directory
   - For production distribution, embed the credentials in `auth.py`

5. **OAuth Consent Screen:**
   - Configure the OAuth consent screen
   - Add scopes: `https://www.googleapis.com/auth/drive`
   - For public distribution, submit for verification

## 📝 Development

### Project Structure

```
gdup/
├── gdup/
│   ├── __init__.py         # Package initialization
│   ├── __main__.py         # Entry point
│   ├── cli.py              # CLI interface
│   ├── auth.py             # OAuth authentication
│   ├── drive.py            # Google Drive API helpers
│   ├── config.py           # Configuration management
│   └── commands/
│       ├── __init__.py
│       ├── ls.py           # List command
│       ├── tree.py         # Tree command
│       ├── cd.py           # Change directory
│       ├── pwd.py          # Print working directory
│       ├── upload.py       # Upload command
│       └── link.py         # Link command
├── installer/
│   └── windows.iss         # Inno Setup script
├── install-linux.sh        # Linux installation script
├── build_windows.py        # Windows build script
├── pyproject.toml          # Project metadata
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

### Running in Development

```bash
# Install in editable mode
pip install -e .

# Run directly
python -m gdup login
python -m gdup ls
```

### Running Tests

```bash
pip install pytest
pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚧 Roadmap

Future features planned for gdup:

- [ ] `gdup down` - Download files from Drive
- [ ] `gdup rm` - Delete files
- [ ] `gdup mv` - Move/rename files
- [ ] `gdup cp` - Copy files
- [ ] Folder synchronization
- [ ] File encryption before upload
- [ ] Interactive shell mode (`gdup shell`)
- [ ] Search functionality
- [ ] Trash management
- [ ] Shared drive support
- [ ] Multiple account support

## ❓ FAQ

**Q: Do I need to create a Google Cloud project?**  
A: No! As an end user, you just install and run `gdup login`. The developer has already set up the OAuth credentials.

**Q: Is my data secure?**  
A: Yes. gdup uses Google's official OAuth 2.0 flow. Your credentials are stored locally and never sent to any third party.

**Q: Can I use this for large files?**  
A: Yes! gdup supports resumable uploads for large files and shows progress.

**Q: What happens if I uninstall gdup?**  
A: Your tokens and configuration remain in the config directory, so you won't need to re-authenticate if you reinstall.

**Q: Can I use this in scripts?**  
A: Yes! gdup is designed to be script-friendly. Just make sure to authenticate first.

## 🐛 Troubleshooting

**"credentials.json not found"**  
- This error appears in development. You need to obtain OAuth credentials from Google Cloud Console.
- For end users, this should not appear in the distributed version.

**"Not authenticated with Google Drive"**  
- Run `gdup login` to authenticate.

**"Permission denied"**  
- On Linux, you may need to add execute permission: `chmod +x ~/.local/bin/gdup`

**PATH not found after installation (Windows)**  
- Restart your terminal or command prompt
- If still not working, log out and log back in

**PATH not found after installation (Linux)**  
- Make sure `~/.local/bin` is in your PATH
- Add to `~/.bashrc`: `export PATH="$HOME/.local/bin:$PATH"`
- Run `source ~/.bashrc`

## 📧 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub](https://github.com/yourusername/gdup/issues)
- Check existing issues for solutions

---

<p align="center">Made with ❤️ from DND for easier Google Drive management</p>
