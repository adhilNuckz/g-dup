"""Google OAuth authentication for DUP."""

import os
import json
from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from .config import get_token_path

# If modifying these scopes, delete token.json
SCOPES = ['https://www.googleapis.com/auth/drive']


def get_credentials_json() -> dict:
   
    # Check if credentials.json exists in the same directory as this script
    script_dir = Path(__file__).parent
    creds_file = script_dir / 'credentials.json'
    
    if creds_file.exists():
        with open(creds_file, 'r') as f:
            return json.load(f)
    
    # For production, credentials should be embedded here
    # This is a placeholder - replace with actual credentials before distribution
    raise FileNotFoundError(
        "credentials.json not found. Please place it in the dup/ directory.\n"
        "See README for instructions on obtaining OAuth credentials."
    )


def authenticate() -> Credentials:
    """
    Authenticate with Google Drive using OAuth 2.0.
    
    Returns:
        Credentials object for Google API access
    """
    creds = None
    token_path = get_token_path()
    
    # Load existing token if available
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    
    # If there are no (valid) credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                # Refresh failed, need to re-authenticate
                creds = None
        
        if not creds:
            credentials_json = get_credentials_json()
            flow = InstalledAppFlow.from_client_config(
                credentials_json,
                SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    return creds


def get_drive_service():
    """
    Get authenticated Google Drive service.
    
    Returns:
        Google Drive API service object
    """
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    return service


def is_authenticated() -> bool:
    """Check if user is already authenticated."""
    token_path = get_token_path()
    if not token_path.exists():
        return False
    
    try:
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
        return creds.valid or (creds.expired and creds.refresh_token)
    except Exception:
        return False
