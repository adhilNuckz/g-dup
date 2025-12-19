"""Google Drive API helper functions."""

import io
import os
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload, MediaIoBaseUpload
from googleapiclient.errors import HttpError
from .auth import get_drive_service


def list_files(folder_id: str = 'root', page_size: int = 100) -> List[Dict[str, Any]]:
    """
    List files in a specific folder.
    
    Args:
        folder_id: ID of the folder to list (default: root)
        page_size: Maximum number of files to return
    
    Returns:
        List of file metadata dictionaries
    """
    service = get_drive_service()
    
    query = f"'{folder_id}' in parents and trashed=false"
    
    # Retry logic for SSL errors
    max_retries = 3
    for attempt in range(max_retries):
        try:
            results = service.files().list(
                q=query,
                pageSize=page_size,
                fields="files(id, name, mimeType, size, modifiedTime, webViewLink)",
                orderBy="folder,name"
            ).execute()
            
            return results.get('files', [])
        except (ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                time.sleep(1)  # Wait before retry
                continue
            raise Exception(f"Connection error after {max_retries} attempts. Please check your internet connection.")


def get_file_by_name(name: str, parent_id: str = 'root') -> Optional[Dict[str, Any]]:
    """
    Get a file or folder by name in a specific parent folder.
    
    Args:
        name: Name of the file/folder
        parent_id: ID of the parent folder
    
    Returns:
        File metadata dictionary or None if not found
    """
    service = get_drive_service()
    
    query = f"name='{name}' and '{parent_id}' in parents and trashed=false"
    
    # Retry logic for SSL errors
    max_retries = 3
    for attempt in range(max_retries):
        try:
            results = service.files().list(
                q=query,
                pageSize=1,
                fields="files(id, name, mimeType, size, modifiedTime, webViewLink)"
            ).execute()
            
            files = results.get('files', [])
            return files[0] if files else None
        except (ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            return None


def get_file_by_id(file_id: str) -> Optional[Dict[str, Any]]:
    """
    Get file metadata by ID.
    
    Args:
        file_id: ID of the file
    
    Returns:
        File metadata dictionary
    """
    service = get_drive_service()
    
    # Retry logic for SSL errors
    max_retries = 3
    for attempt in range(max_retries):
        try:
            file = service.files().get(
                fileId=file_id,
                fields="id, name, mimeType, size, modifiedTime, webViewLink, parents"
            ).execute()
            return file
        except (ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            return None
        except Exception:
            return None


def is_folder(file_metadata: Dict[str, Any]) -> bool:
    """Check if a file is a folder."""
    return file_metadata.get('mimeType') == 'application/vnd.google-apps.folder'


def create_folder(name: str, parent_id: str = 'root') -> Dict[str, Any]:
    """
    Create a folder in Google Drive.
    
    Args:
        name: Name of the folder
        parent_id: ID of the parent folder
    
    Returns:
        Created folder metadata
    """
    service = get_drive_service()
    
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    
    # Retry logic for SSL errors
    max_retries = 3
    for attempt in range(max_retries):
        try:
            folder = service.files().create(
                body=file_metadata,
                fields='id, name, mimeType'
            ).execute()
            return folder
        except (ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            raise Exception(f"Connection error after {max_retries} attempts. Please check your internet connection.")


def upload_file(file_path: str, parent_id: str = 'root', callback=None) -> Dict[str, Any]:
    """
    Upload a file to Google Drive.
    
    Args:
        file_path: Local path to the file
        parent_id: ID of the parent folder
        callback: Progress callback function
    
    Returns:
        Uploaded file metadata
    """
    service = get_drive_service()
    
    file_name = os.path.basename(file_path)
    
    file_metadata = {
        'name': file_name,
        'parents': [parent_id]
    }
    
    media = MediaFileUpload(
        file_path,
        resumable=True
    )
    
    request = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, name, mimeType, size, webViewLink'
    )
    
    response = None
    max_retries = 3
    
    while response is None:
        for attempt in range(max_retries):
            try:
                status, response = request.next_chunk()
                if status and callback:
                    callback(status.progress())
                break  # Success, exit retry loop
            except (ConnectionError, OSError) as e:
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                raise Exception(f"Connection error after {max_retries} attempts. Please check your internet connection.")
    
    return response


def upload_folder(folder_path: str, parent_id: str = 'root', callback=None) -> Dict[str, Any]:
    """
    Upload a folder and its contents recursively.
    
    Args:
        folder_path: Local path to the folder
        parent_id: ID of the parent folder
        callback: Progress callback function
    
    Returns:
        Created folder metadata
    """
    folder_name = os.path.basename(folder_path)
    
    # Create the folder in Drive
    folder_metadata = create_folder(folder_name, parent_id)
    folder_id = folder_metadata['id']
    
    # Upload all contents
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        if os.path.isfile(item_path):
            upload_file(item_path, folder_id, callback)
        elif os.path.isdir(item_path):
            upload_folder(item_path, folder_id, callback)
    
    return folder_metadata


def get_file_link(file_id: str) -> str:
    """
    Get the web view link for a file.
    
    Args:
        file_id: ID of the file
    
    Returns:
        Web view link URL
    """
    file = get_file_by_id(file_id)
    return file.get('webViewLink', f'https://drive.google.com/file/d/{file_id}/view')


def make_file_public(file_id: str) -> None:
    """
    Make a file publicly accessible.
    
    Args:
        file_id: ID of the file
    """
    service = get_drive_service()
    
    permission = {
        'type': 'anyone',
        'role': 'reader'
    }
    
    # Retry logic for SSL errors
    max_retries = 3
    for attempt in range(max_retries):
        try:
            service.permissions().create(
                fileId=file_id,
                body=permission
            ).execute()
            return
        except (ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            raise Exception(f"Connection error after {max_retries} attempts. Please check your internet connection.")


def is_file_public(file_id: str) -> bool:
    """
    Check if a file is publicly accessible.
    
    Args:
        file_id: ID of the file
    
    Returns:
        True if file is public, False otherwise
    """
    service = get_drive_service()
    
    # Retry logic for SSL errors
    max_retries = 3
    for attempt in range(max_retries):
        try:
            permissions = service.permissions().list(
                fileId=file_id,
                fields='permissions(type, role)'
            ).execute()
            
            for permission in permissions.get('permissions', []):
                if permission.get('type') == 'anyone':
                    return True
            
            return False
        except (ConnectionError, OSError) as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            return False
        except Exception:
            return False


def build_tree(folder_id: str = 'root', prefix: str = '', is_last: bool = True, max_depth: int = 10, current_depth: int = 0) -> List[str]:
    """
    Build a tree structure of files and folders.
    
    Args:
        folder_id: ID of the folder to start from
        prefix: Prefix for indentation
        is_last: Whether this is the last item in the current level
        max_depth: Maximum recursion depth
        current_depth: Current recursion depth
    
    Returns:
        List of formatted tree lines
    """
    if current_depth >= max_depth:
        return []
    
    try:
        files = list_files(folder_id)
    except Exception as e:
        return [prefix + "└── [Error reading folder]"]
    
    lines = []
    
    for i, file in enumerate(files):
        is_last_item = i == len(files) - 1
        connector = "└── " if is_last_item else "├── "
        
        file_name = file['name']
        if is_folder(file):
            file_name = f"📁 {file_name}"
        else:
            file_name = f"📄 {file_name}"
        
        lines.append(prefix + connector + file_name)
        
        # If it's a folder, recurse
        if is_folder(file):
            extension = "    " if is_last_item else "│   "
            try:
                sub_lines = build_tree(file['id'], prefix + extension, is_last_item, max_depth, current_depth + 1)
                lines.extend(sub_lines)
            except Exception:
                lines.append(prefix + extension + "└── [Error reading subfolder]")
    
    return lines


def resolve_path(path: str, current_folder_id: str = 'root') -> Optional[str]:
    """
    Resolve a path to a folder ID.
    
    Args:
        path: Path to resolve (e.g., "folder1/folder2" or ".." or ".")
        current_folder_id: Current folder ID
    
    Returns:
        Folder ID or None if path doesn't exist
    """
    if path == '.':
        return current_folder_id
    
    if path == '/':
        return 'root'
    
    if path == '..':
        # Get parent folder
        file = get_file_by_id(current_folder_id)
        if not file:
            return None
        parents = file.get('parents', [])
        return parents[0] if parents else 'root'
    
    # Handle absolute paths
    if path.startswith('/'):
        current_folder_id = 'root'
        path = path[1:]
    
    # Handle relative paths
    if not path:
        return current_folder_id
    
    parts = path.split('/')
    
    for part in parts:
        if not part or part == '.':
            continue
        
        if part == '..':
            file = get_file_by_id(current_folder_id)
            if not file:
                return None
            parents = file.get('parents', [])
            current_folder_id = parents[0] if parents else 'root'
        else:
            file = get_file_by_name(part, current_folder_id)
            if not file or not is_folder(file):
                return None
            current_folder_id = file['id']
    
    return current_folder_id


def download_file(file_id: str, destination_path: str, callback=None) -> str:
    """
    Download a file from Google Drive.
    
    Args:
        file_id: ID of the file to download
        destination_path: Local path where file should be saved
        callback: Progress callback function
    
    Returns:
        Path to downloaded file
    """
    service = get_drive_service()
    
    # Get file metadata
    file_metadata = get_file_by_id(file_id)
    if not file_metadata:
        raise FileNotFoundError(f"File not found: {file_id}")
    
    # Check if it's a Google Workspace file (Docs, Sheets, etc.)
    mime_type = file_metadata.get('mimeType', '')
    
    # Handle Google Workspace files by exporting them
    if mime_type.startswith('application/vnd.google-apps.'):
        export_mimetypes = {
            'application/vnd.google-apps.document': ('application/pdf', '.pdf'),
            'application/vnd.google-apps.spreadsheet': ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', '.xlsx'),
            'application/vnd.google-apps.presentation': ('application/vnd.openxmlformats-officedocument.presentationml.presentation', '.pptx'),
        }
        
        export_info = export_mimetypes.get(mime_type)
        if export_info:
            export_mimetype, extension = export_info
            request = service.files().export_media(fileId=file_id, mimeType=export_mimetype)
            
            # Add extension if not present
            if not destination_path.endswith(extension):
                destination_path += extension
        else:
            raise ValueError(f"Cannot download Google Apps file of type: {mime_type}")
    else:
        # Regular file download
        request = service.files().get_media(fileId=file_id)
    
    # Download with progress
    with open(destination_path, 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        max_retries = 3
        
        while not done:
            for attempt in range(max_retries):
                try:
                    status, done = downloader.next_chunk()
                    if status and callback:
                        callback(status.progress())
                    break  # Success, exit retry loop
                except (ConnectionError, OSError) as e:
                    if attempt < max_retries - 1:
                        time.sleep(1)
                        continue
                    raise Exception(f"Connection error after {max_retries} attempts. Please check your internet connection.")
    
    return destination_path


def get_full_path(folder_id: str) -> str:
    """
    Get the full path of a folder.
    
    Args:
        folder_id: ID of the folder
    
    Returns:
        Full path string (e.g., "/folder1/folder2")
    """
    if folder_id == 'root':
        return '/'
    
    path_parts = []
    current_id = folder_id
    
    while current_id != 'root':
        file = get_file_by_id(current_id)
        if not file:
            break
        
        path_parts.insert(0, file['name'])
        parents = file.get('parents', [])
        if not parents:
            break
        current_id = parents[0]
    
    return '/' + '/'.join(path_parts) if path_parts else '/'
