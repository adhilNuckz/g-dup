"""Change directory command."""

import typer
from rich.console import Console
from ..drive import resolve_path, get_full_path, is_folder, get_file_by_id
from ..config import get_current_folder_id, set_current_folder

console = Console()


def cd_command(path: str):
    """Change current Drive folder."""
    try:
        current_folder_id = get_current_folder_id()
        
        # Resolve the path
        new_folder_id = resolve_path(path, current_folder_id)
        
        if not new_folder_id:
            console.print(f"[red]Error:[/red] Path not found: {path}")
            raise typer.Exit(1)
        
        # Verify it's a folder (or root)
        if new_folder_id != 'root':
            file = get_file_by_id(new_folder_id)
            if not file or not is_folder(file):
                console.print(f"[red]Error:[/red] Not a folder: {path}")
                raise typer.Exit(1)
        
        # Get the full path
        new_path = get_full_path(new_folder_id)
        
        # Save the new location
        set_current_folder(new_folder_id, new_path)
        
        console.print(f"[green]Changed to:[/green] [cyan]{new_path}[/cyan]")
        
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
