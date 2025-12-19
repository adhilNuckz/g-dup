"""Configuration management for DUP."""

import json
import os
from pathlib import Path
from typing import Dict, Any


def get_config_dir() -> Path:
    """Get the configuration directory based on OS."""
    if os.name == 'nt':  # Windows
        config_dir = Path(os.getenv('APPDATA')) / 'dup'
    else:  # Linux/Unix
        config_dir = Path.home() / '.config' / 'dup'
    
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def get_token_path() -> Path:
    """Get the path to the token file."""
    return get_config_dir() / 'token.json'


def get_state_path() -> Path:
    """Get the path to the state file."""
    return get_config_dir() / 'state.json'


def load_state() -> Dict[str, Any]:
    """Load current state (current folder, path, etc.)."""
    state_path = get_state_path()
    
    if state_path.exists():
        with open(state_path, 'r') as f:
            return json.load(f)
    
    # Default state
    return {
        "current_folder_id": "root",
        "current_path": "/"
    }


def save_state(state: Dict[str, Any]) -> None:
    """Save current state to disk."""
    state_path = get_state_path()
    with open(state_path, 'w') as f:
        json.dump(state, f, indent=2)


def get_current_folder_id() -> str:
    """Get the current folder ID."""
    state = load_state()
    return state.get("current_folder_id", "root")


def get_current_path() -> str:
    """Get the current Drive path."""
    state = load_state()
    return state.get("current_path", "/")


def set_current_folder(folder_id: str, path: str) -> None:
    """Set the current folder ID and path."""
    state = load_state()
    state["current_folder_id"] = folder_id
    state["current_path"] = path
    save_state(state)
