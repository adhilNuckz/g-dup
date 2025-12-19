# Developer Guide - DUP

## Setting Up Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/dup.git
cd dup
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install package in editable mode with dev dependencies
pip install -e ".[dev]"
```

### 4. Set Up OAuth Credentials

To develop and test DUP, you need Google OAuth credentials:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the Google Drive API
4. Create OAuth 2.0 credentials (Desktop app type)
5. Download `credentials.json`
6. Place it in the `dup/` directory

**IMPORTANT**: Never commit `credentials.json` to version control!

## Running in Development

```bash
# Run the CLI
python -m dup login
python -m dup ls
python -m dup up test.txt

# Or use the installed command
dup login
dup ls
```

## Code Structure

### Core Modules

**`auth.py`**
- Handles OAuth 2.0 authentication
- Manages token storage and refresh
- Provides `get_drive_service()` for API access

**`config.py`**
- Manages configuration directory
- Handles state persistence (current folder, path)
- Cross-platform path handling

**`drive.py`**
- Google Drive API wrapper functions
- File/folder operations (list, upload, create, etc.)
- Path resolution and navigation
- Tree building for visualization

**`cli.py`**
- Main CLI entry point using Typer
- Command routing
- Authentication check middleware

### Commands

Each command is in its own module under `dup/commands/`:

- `ls.py` - List files with formatted table
- `tree.py` - Recursive folder visualization
- `cd.py` - Change directory with path resolution
- `pwd.py` - Print working directory
- `upload.py` - File/folder upload with progress
- `link.py` - Generate shareable links with privacy control

## Adding New Commands

1. Create a new file in `dup/commands/`, e.g., `download.py`:

```python
"""Download command."""

import typer
from rich.console import Console

console = Console()

def download_command(filename: str, destination: str = "."):
    """Download a file from Drive."""
    try:
        # Your implementation here
        console.print(f"[green]✓ Downloaded:[/green] {filename}")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
```

2. Add the command to `cli.py`:

```python
from .commands.download import download_command

@app.command()
def down(
    filename: str = typer.Argument(..., help="File to download"),
    destination: str = typer.Option(".", help="Download destination")
):
    """Download a file from Drive."""
    download_command(filename, destination)
```

## Testing

### Manual Testing

```bash
# Test authentication
python -m dup login

# Test navigation
python -m dup ls
python -m dup cd Documents
python -m dup pwd

# Test upload
echo "test" > test.txt
python -m dup up test.txt

# Test link
python -m dup link test.txt
```

### Unit Tests (Future)

```bash
pytest tests/
```

## Building

### Windows Executable

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build:
```bash
python build_windows.py
```

3. Output: `dist/dup.exe`

### Windows Installer

1. Install [Inno Setup](https://jrsoftware.org/isinfo.php)

2. Open `installer/windows.iss` in Inno Setup Compiler

3. Update the `AppId` (generate a new GUID)

4. Click "Compile"

5. Output: `dist/dup-setup-1.0.0.exe`

### Linux Installation

```bash
# Install locally
pip install --user .

# Or create binary
pyinstaller --onefile dup/__main__.py --name dup
# Copy dist/dup to /usr/local/bin
```

## Distribution Checklist

Before distributing DUP:

- [ ] Embed OAuth credentials in `auth.py`
- [ ] Update version in `dup/__init__.py`
- [ ] Update version in `pyproject.toml`
- [ ] Update version in `installer/windows.iss`
- [ ] Test on clean Windows installation
- [ ] Test on clean Linux installation
- [ ] Verify PATH is set correctly
- [ ] Verify uninstaller preserves user data
- [ ] Update CHANGELOG
- [ ] Create GitHub release
- [ ] Build and upload installers

## OAuth Credentials for Production

For production distribution, embed credentials in `auth.py`:

```python
def get_credentials_json() -> dict:
    """Get embedded OAuth credentials."""
    return {
        "installed": {
            "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "YOUR_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"]
        }
    }
```

**Security Note**: For public distribution, consider:
- Using OAuth verification from Google
- Rotating client secrets periodically
- Implementing rate limiting
- Adding usage analytics

## Code Style

Follow PEP 8 with these preferences:
- Line length: 100 characters
- Use f-strings for formatting
- Type hints where appropriate
- Docstrings for all functions

Format code:
```bash
black dup/
```

Lint code:
```bash
flake8 dup/
```

## Debugging

### Enable Debug Logging

Add to your code:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Common Issues

**"credentials.json not found"**
- Make sure it's in the `dup/` directory
- Check `.gitignore` isn't excluding it locally

**OAuth errors**
- Verify Drive API is enabled
- Check redirect URIs in Cloud Console
- Ensure client ID/secret are correct

**Import errors**
- Reinstall: `pip install -e .`
- Check virtual environment is activated

## Version Control

### Branching Strategy

- `main` - Stable releases
- `develop` - Development branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `release/*` - Release preparation

### Commit Messages

Follow conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code refactoring
- `test:` - Tests
- `chore:` - Maintenance

Example:
```
feat: add download command for files
fix: resolve path handling on Windows
docs: update installation instructions
```

## Release Process

1. Update version numbers
2. Update CHANGELOG
3. Test thoroughly
4. Build executables
5. Create installer
6. Tag release: `git tag v1.0.0`
7. Push tag: `git push origin v1.0.0`
8. Create GitHub release
9. Upload installers
10. Update documentation

## Contributing Guidelines

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Update documentation
6. Submit pull request

## Resources

- [Google Drive API Docs](https://developers.google.com/drive/api/v3/about-sdk)
- [OAuth 2.0 Flow](https://developers.google.com/identity/protocols/oauth2)
- [Typer Documentation](https://typer.tiangolo.com/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [PyInstaller Manual](https://pyinstaller.org/en/stable/)
- [Inno Setup Documentation](https://jrsoftware.org/ishelp/)

## Getting Help

- Open an issue on GitHub
- Check existing issues and PRs
- Read the documentation
- Review the code comments

Happy coding! 🚀
