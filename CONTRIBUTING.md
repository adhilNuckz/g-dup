# Contributing to DUP

First off, thank you for considering contributing to DUP! It's people like you that make DUP such a great tool.

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots if possible**
* **Include your environment details**:
  - OS: Windows/Linux
  - Python version
  - DUP version

**Bug Report Template:**
```markdown
**Description:**
A clear and concise description of the bug.

**Steps to Reproduce:**
1. Run command '...'
2. Navigate to '...'
3. See error

**Expected Behavior:**
What you expected to happen.

**Actual Behavior:**
What actually happened.

**Environment:**
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python Version: [e.g., 3.11.5]
- DUP Version: [e.g., 1.0.0]

**Additional Context:**
Any other information about the problem.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and explain the behavior you expected to see instead**
* **Explain why this enhancement would be useful**

**Enhancement Template:**
```markdown
**Feature Description:**
A clear and concise description of the feature.

**Use Case:**
Describe the problem this feature would solve.

**Proposed Solution:**
Describe how you envision this feature working.

**Alternative Solutions:**
Describe any alternative solutions you've considered.

**Additional Context:**
Any other information about the feature request.
```

### Pull Requests

* Fill in the required template
* Follow the Python style guide (PEP 8)
* Include thoughtful comments in your code
* End all files with a newline
* Write meaningful commit messages
* Update documentation as needed

## 🚀 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/dup.git
cd dup
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux:
source venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

### 3. Get OAuth Credentials

See [SETUP.md](SETUP.md) for detailed instructions on obtaining Google OAuth credentials.

### 4. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/your-bug-fix
```

## 💻 Coding Guidelines

### Python Style Guide

* Follow PEP 8
* Use meaningful variable and function names
* Add docstrings to all functions and classes
* Keep functions small and focused
* Use type hints where appropriate

### Code Example

```python
"""Module for handling file uploads."""

from typing import Optional
from pathlib import Path


def upload_file(file_path: str, parent_id: str = 'root') -> dict:
    """
    Upload a file to Google Drive.
    
    Args:
        file_path: Local path to the file
        parent_id: ID of the parent folder (default: root)
    
    Returns:
        Dictionary containing uploaded file metadata
        
    Raises:
        FileNotFoundError: If file_path doesn't exist
        PermissionError: If file cannot be read
    """
    # Implementation here
    pass
```

### Commit Message Format

Use conventional commits format:

```
type(scope): subject

body

footer
```

**Types:**
* `feat`: New feature
* `fix`: Bug fix
* `docs`: Documentation changes
* `style`: Code style changes (formatting, etc.)
* `refactor`: Code refactoring
* `test`: Adding or updating tests
* `chore`: Maintenance tasks

**Examples:**
```
feat(upload): add support for resumable uploads

Implement resumable upload functionality for large files
using MediaFileUpload with resumable=True.

Closes #123
```

```
fix(auth): handle token refresh failure

Add try-catch block to handle token refresh failures
and re-authenticate when refresh fails.

Fixes #456
```

### Directory Structure for New Features

When adding new commands:

1. Create module in `dup/commands/`
2. Implement command function
3. Register in `dup/cli.py`
4. Update documentation

Example:
```python
# dup/commands/download.py
"""Download command implementation."""

import typer
from rich.console import Console

console = Console()

def download_command(filename: str, destination: str = "."):
    """Download a file from Drive."""
    try:
        # Implementation
        console.print(f"[green]✓ Downloaded:[/green] {filename}")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
```

```python
# dup/cli.py (add this)
from .commands.download import download_command

@app.command()
def down(
    filename: str = typer.Argument(..., help="File to download"),
    destination: str = typer.Option(".", help="Download destination")
):
    """Download a file from Drive."""
    download_command(filename, destination)
```

## 🧪 Testing

### Manual Testing

```bash
# Test your changes
python -m dup login
python -m dup ls
python -m dup up test.txt
# etc.
```

### Adding Tests (Future)

When we add automated tests:

```python
# tests/test_upload.py
import pytest
from dup.commands.upload import upload_command

def test_upload_file():
    """Test file upload functionality."""
    # Test implementation
    pass
```

## 📝 Documentation

### Update Documentation

When making changes, update relevant documentation:

* **README.md** - User-facing features
* **DEVELOPER.md** - Developer-specific info
* **CHANGELOG.md** - Version history
* **Docstrings** - Code documentation

### Documentation Style

* Use clear, concise language
* Include code examples
* Add screenshots for UI changes
* Use proper Markdown formatting

## 🔄 Pull Request Process

### Before Submitting

1. **Test thoroughly**: Make sure your changes work
2. **Update documentation**: Reflect your changes in docs
3. **Check code style**: Follow PEP 8
4. **Write good commit messages**: Use conventional commits
5. **Update CHANGELOG**: Add entry for your change

### Submitting

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request on GitHub**

3. **Fill in the PR template**:
   ```markdown
   **Description:**
   Brief description of changes
   
   **Type of Change:**
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Code refactoring
   
   **Testing:**
   How has this been tested?
   
   **Checklist:**
   - [ ] Code follows style guidelines
   - [ ] Documentation updated
   - [ ] CHANGELOG updated
   - [ ] All tests pass
   
   **Related Issues:**
   Closes #123
   ```

4. **Wait for review**: Maintainers will review your PR

5. **Address feedback**: Make requested changes if any

6. **Merge**: Once approved, your PR will be merged!

## 🏷️ Issue and PR Labels

We use labels to organize issues and PRs:

* `bug` - Something isn't working
* `enhancement` - New feature or request
* `documentation` - Documentation improvements
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention needed
* `question` - Further information requested
* `wontfix` - This will not be worked on
* `duplicate` - This issue/PR already exists
* `invalid` - This doesn't seem right

## 💬 Communication

* **GitHub Issues**: For bugs and feature requests
* **Pull Requests**: For code contributions
* **Discussions**: For general questions and ideas

## 🎯 Priorities

Current priority areas for contributions:

1. **Testing**: Unit tests, integration tests
2. **Download functionality**: `dup down` command
3. **File management**: Delete, move, copy commands
4. **Documentation**: Improvements and translations
5. **Bug fixes**: Check open issues

## ⚖️ Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior:**
* Using welcoming and inclusive language
* Being respectful of differing viewpoints
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards others

**Unacceptable behavior:**
* Trolling, insulting/derogatory comments
* Public or private harassment
* Publishing others' private information
* Other conduct which could reasonably be considered inappropriate

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by opening an issue or contacting the project maintainers. All complaints will be reviewed and investigated promptly and fairly.

## 🙏 Recognition

Contributors will be recognized in:
* CHANGELOG.md for their contributions
* GitHub contributors page
* Special mentions for significant contributions

## ❓ Questions?

If you have questions about contributing:
* Check existing documentation
* Search closed issues
* Open a new issue with the `question` label
* Reach out to maintainers

## 📚 Resources

* [Python Style Guide (PEP 8)](https://pep8.org/)
* [Conventional Commits](https://www.conventionalcommits.org/)
* [Google Drive API Documentation](https://developers.google.com/drive/api/v3/about-sdk)
* [Typer Documentation](https://typer.tiangolo.com/)
* [Rich Documentation](https://rich.readthedocs.io/)

---

Thank you for contributing to DUP! 🎉

Every contribution, no matter how small, makes a difference.
