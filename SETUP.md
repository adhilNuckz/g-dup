# Getting Started with DUP Development

## Prerequisites Setup

Before you can use DUP, you need to obtain Google OAuth credentials. This is a one-time setup for developers.

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Enter project name: "DUP Development"
4. Click "Create"

### Step 2: Enable Google Drive API

1. In your project, go to "APIs & Services" → "Library"
2. Search for "Google Drive API"
3. Click on it and click "Enable"

### Step 3: Configure OAuth Consent Screen

1. Go to "APIs & Services" → "OAuth consent screen"
2. Select "External" (or "Internal" if you have a Google Workspace)
3. Click "Create"
4. Fill in:
   - App name: "DUP - Drive Upload Program"
   - User support email: (your email)
   - Developer contact: (your email)
5. Click "Save and Continue"
6. On "Scopes", click "Add or Remove Scopes"
7. Search for "Google Drive API"
8. Select: `https://www.googleapis.com/auth/drive`
9. Click "Update" → "Save and Continue"
10. On "Test users", add your email address
11. Click "Save and Continue"

### Step 4: Create OAuth Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. Application type: "Desktop app"
4. Name: "DUP Desktop Client"
5. Click "Create"
6. Click "Download JSON"
7. Rename the downloaded file to `credentials.json`
8. Move it to the `dup/` directory in your project

**Important**: Add `dup/credentials.json` to `.gitignore` (already done)

### Step 5: Install and Test

```bash
# Install in development mode
pip install -e .

# Test authentication
dup login
```

This will:
- Open your browser
- Ask you to sign in with Google
- Show a warning (because app is not verified - this is normal for development)
- Click "Advanced" → "Go to DUP (unsafe)"
- Grant permissions
- Save token to your config directory

### Step 6: Test Commands

```bash
# List files
dup ls

# Navigate
dup cd Documents

# Show path
dup pwd

# Upload a test file
echo "test" > test.txt
dup up test.txt

# Get link
dup link test.txt

# Show tree
dup tree
```

## For Production Distribution

When distributing DUP to end users:

1. **Embed credentials in code**: Modify `dup/auth.py` to return credentials directly instead of reading from file:

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

2. **Get OAuth verification**: For public distribution, submit your app for OAuth verification to remove the "unsafe" warning.

3. **Build executable**: Follow instructions in DEVELOPER.md

## Troubleshooting

**"credentials.json not found"**
- Make sure the file is in the `dup/` directory
- Check the filename (must be exactly `credentials.json`)

**"Access blocked: This app's request is invalid"**
- Make sure you enabled the Google Drive API
- Check that you selected the correct scopes

**"redirect_uri_mismatch"**
- The default redirect URI should be `http://localhost`
- This is automatically handled by the OAuth library

**Browser doesn't open**
- Check if a firewall is blocking the local server
- Try manually opening the URL shown in the terminal

**"Invalid grant" error**
- Delete the token file and re-authenticate:
  - Windows: `del %APPDATA%\dup\token.json`
  - Linux: `rm ~/.config/dup/token.json`
- Run `dup login` again

## Security Notes

- Never commit `credentials.json` to version control
- Never share your `client_secret` publicly
- For production, consider:
  - OAuth verification from Google
  - Rate limiting
  - Usage monitoring
  - Periodic credential rotation

## Next Steps

Once you have DUP working:

1. Read [README.md](README.md) for user documentation
2. Read [DEVELOPER.md](DEVELOPER.md) for development guidelines
3. Read [QUICKSTART.md](QUICKSTART.md) for common usage patterns
4. Start building new features!

## Questions?

Open an issue on GitHub or check the documentation.

Happy developing! 🚀
