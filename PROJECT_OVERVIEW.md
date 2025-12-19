# DUP Project Overview

## 📁 Project Structure

```
dup/
├── 📂 dup/                          # Main package directory
│   ├── __init__.py                  # Package initialization (version info)
│   ├── __main__.py                  # Entry point for `python -m dup`
│   ├── cli.py                       # Main CLI application (Typer)
│   ├── auth.py                      # Google OAuth authentication
│   ├── drive.py                     # Google Drive API helpers
│   ├── config.py                    # Configuration management
│   ├── credentials.json.example     # Example credentials file
│   └── 📂 commands/                 # Command implementations
│       ├── __init__.py
│       ├── ls.py                    # List files command
│       ├── tree.py                  # Tree view command
│       ├── cd.py                    # Change directory command
│       ├── pwd.py                   # Print working directory
│       ├── upload.py                # Upload files/folders
│       └── link.py                  # Generate shareable links
│
├── 📂 installer/                    # Installation scripts
│   └── windows.iss                  # Inno Setup script for Windows
│
├── 📄 pyproject.toml                # Project metadata & dependencies
├── 📄 requirements.txt              # Python dependencies
├── 📄 build_windows.py              # PyInstaller build script
├── 📄 install-linux.sh              # Linux installation script
├── 📄 .gitignore                    # Git ignore rules
├── 📄 LICENSE                       # MIT License
│
└── 📚 Documentation/
    ├── README.md                    # Main documentation
    ├── QUICKSTART.md                # Quick start guide
    ├── SETUP.md                     # Development setup guide
    ├── DEVELOPER.md                 # Developer guide
    └── CHANGELOG.md                 # Version history
```

## 🎯 Architecture

### Core Components

#### 1. **Authentication Layer** (`auth.py`)
- Handles OAuth 2.0 flow
- Token management (storage, refresh)
- Provides authenticated Google Drive service
- Zero user setup required

#### 2. **Drive API Layer** (`drive.py`)
- Wrapper around Google Drive API v3
- Operations: list, upload, create folder, get file, etc.
- Path resolution and navigation
- Tree structure building
- Link generation and sharing

#### 3. **Configuration Layer** (`config.py`)
- Cross-platform config directory management
- State persistence (current folder, path)
- Token storage paths
- JSON-based state file

#### 4. **CLI Layer** (`cli.py`)
- Typer-based command routing
- Authentication middleware
- Version information
- Help system

#### 5. **Commands** (`commands/`)
- Modular command implementations
- Rich UI (tables, progress bars, colors)
- Error handling
- User confirmations for sensitive operations

## 🔄 Data Flow

### Command Execution Flow

```
User Input (CLI)
    ↓
cli.py (Typer App)
    ↓
Authentication Check
    ↓
Command Module (ls, cd, up, etc.)
    ↓
Drive API Helper (drive.py)
    ↓
Google Drive API
    ↓
Response Processing
    ↓
Rich UI Output (Console)
```

### Authentication Flow

```
User runs `dup login`
    ↓
Check if token exists (config.py)
    ↓
Token valid? 
├─ Yes → Use existing token
└─ No  → OAuth flow
    ↓
Open browser
    ↓
User authenticates with Google
    ↓
Token saved locally (auth.py)
    ↓
Ready to use!
```

### Upload Flow

```
User runs `dup up myfile.pdf`
    ↓
Verify file exists (upload.py)
    ↓
Get current folder ID (config.py)
    ↓
Upload with progress (drive.py)
    ├─ MediaFileUpload
    └─ Progress callback → tqdm bar
    ↓
Display result + link
```

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.8+**: Main language
- **Typer**: CLI framework
- **Rich**: Terminal UI (colors, tables, progress)
- **tqdm**: Upload progress bars
- **Google APIs**: 
  - `google-auth`: Authentication
  - `google-auth-oauthlib`: OAuth flow
  - `google-api-python-client`: Drive API

### Build & Distribution
- **PyInstaller**: Create standalone executables
- **Inno Setup**: Windows installer
- **setuptools**: Python packaging

## 📦 Packaging

### Windows Distribution
1. **Build executable**: PyInstaller creates `dup.exe`
2. **Create installer**: Inno Setup packages exe
3. **Installer features**:
   - Copies to Program Files
   - Adds to PATH automatically
   - Creates uninstaller
   - Preserves user data on uninstall

### Linux Distribution
1. **Source distribution**: Git repository
2. **Installation methods**:
   - pip install from source
   - Or standalone binary via PyInstaller
3. **Installation location**: `~/.local/bin/`

## 💾 State Management

### Configuration Files

**Windows**: `%APPDATA%\dup\`
**Linux**: `~/.config/dup/`

Files:
- `token.json`: OAuth token (auto-refreshed)
- `state.json`: Current folder state

**state.json structure**:
```json
{
  "current_folder_id": "1a2b3c4d5e",
  "current_path": "/Documents/Projects"
}
```

### State Operations
- Load state on command execution
- Save state on `cd` command
- Persist across sessions
- Isolated per user

## 🔐 Security Model

### Authentication
- OAuth 2.0 Desktop App flow
- Developer-owned credentials (embedded)
- User-owned tokens (stored locally)
- No third-party access

### Privacy
- Tokens stored locally only
- No telemetry or tracking
- Link sharing asks for confirmation
- User controls all operations

### Distribution Security
- Credentials embedded in production build
- Client secret protected by OAuth flow
- Rate limiting (Google's)
- Scope limited to Drive access

## 🎨 User Experience

### Design Principles
1. **Filesystem-like**: Familiar commands (ls, cd, pwd)
2. **Zero setup**: No configuration needed
3. **Clear feedback**: Progress bars, colors, confirmations
4. **Safe defaults**: Ask before making files public
5. **Cross-platform**: Same experience on Windows/Linux

### UI Elements
- **Tables**: File listings with type, size, date
- **Progress bars**: Upload progress
- **Colors**: 
  - Green: Success
  - Red: Errors
  - Yellow: Warnings
  - Cyan: Info
- **Icons**: 📁 folders, 📄 files, ✓ success, ⚠️ warnings

## 🚀 Future Enhancements

### Planned Features (v2.0)
- Download files (`dup down`)
- Delete files (`dup rm`)
- Move/rename (`dup mv`)
- Copy files (`dup cp`)
- Search (`dup search`)

### Advanced Features (v3.0)
- Folder synchronization
- File encryption
- Interactive shell mode
- Shared drives support
- Multiple accounts

## 📊 Command Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `login` | Authenticate | `dup login` |
| `ls` | List files | `dup ls Documents` |
| `tree` | Show structure | `dup tree` |
| `cd` | Change folder | `dup cd /Projects` |
| `pwd` | Current path | `dup pwd` |
| `up` | Upload | `dup up file.pdf` |
| `link` | Share link | `dup link file.pdf` |
| `version` | Version info | `dup version` |

## 🔧 Development Workflow

### Setup
1. Clone repository
2. Create virtual environment
3. Install in editable mode: `pip install -e .`
4. Get OAuth credentials (see SETUP.md)
5. Place `credentials.json` in `dup/`

### Testing
1. Run `dup login`
2. Test each command manually
3. Verify cross-platform paths
4. Check error handling

### Building
1. Update version in 3 places:
   - `dup/__init__.py`
   - `pyproject.toml`
   - `installer/windows.iss`
2. Build executable: `python build_windows.py`
3. Create installer: Compile `windows.iss`
4. Test installation on clean system

### Release
1. Update CHANGELOG.md
2. Tag release: `git tag v1.0.0`
3. Build distributables
4. Create GitHub release
5. Upload installers
6. Update documentation

## 📚 Documentation Map

| Document | Audience | Purpose |
|----------|----------|---------|
| README.md | End users | Complete user guide |
| QUICKSTART.md | New users | Quick start tutorial |
| SETUP.md | Developers | OAuth setup guide |
| DEVELOPER.md | Contributors | Development guide |
| CHANGELOG.md | All | Version history |

## 🐛 Common Issues

### Development
- **Missing credentials**: Get from Google Cloud Console
- **Import errors**: Reinstall with `pip install -e .`
- **OAuth errors**: Check API enabled, scopes correct

### Deployment
- **PATH not set**: Windows installer should add it
- **Token expired**: Auto-refresh should handle it
- **Permission denied**: Check file permissions

### User Issues
- **"Not authenticated"**: Run `dup login`
- **"File not found"**: Check current path with `dup pwd`
- **"Permission denied"**: File permissions on Drive

## 📈 Project Status

**Current Version**: 1.0.0  
**Status**: Production Ready  
**Platforms**: Windows, Linux  
**Python**: 3.8+  

### Completed ✅
- [x] OAuth authentication
- [x] File navigation (ls, cd, pwd, tree)
- [x] File upload
- [x] Link generation
- [x] Cross-platform support
- [x] Windows installer
- [x] Linux installation
- [x] Documentation

### In Progress 🚧
- [ ] Unit tests
- [ ] CI/CD pipeline
- [ ] OAuth verification

### Planned 📋
- [ ] Download functionality
- [ ] File deletion
- [ ] File management (mv, cp)
- [ ] Search features
- [ ] Sync capabilities

## 🤝 Contributing

See [DEVELOPER.md](DEVELOPER.md) for:
- Code style guidelines
- Branching strategy
- Commit message format
- Pull request process

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

**Built with ❤️ for easier Google Drive management**
