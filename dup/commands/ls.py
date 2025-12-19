"""List files command."""

import typer
from rich.console import Console
from rich.table import Table
from ..drive import list_files, is_folder
from ..config import get_current_folder_id, get_current_path

console = Console()


def format_size(size) -> str:
    """Format file size in human-readable format."""
    if size is None:
        return "-"
    
    # Convert to int if it's a string
    try:
        size = int(size)
    except (ValueError, TypeError):
        return "-"
    
    size = float(size)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} PB"


def ls_command(path: str = None):
    """List files in current or specified Drive folder."""
    try:
        folder_id = get_current_folder_id()
        current_path = get_current_path()
        
        # If path is provided, resolve it
        if path:
            from ..drive import resolve_path, get_full_path
            folder_id = resolve_path(path, folder_id)
            if not folder_id:
                console.print(f"[red]Error:[/red] Path not found: {path}")
                raise typer.Exit(1)
            current_path = get_full_path(folder_id)
        
        console.print(f"[cyan]📂 {current_path}[/cyan]\n")
        
        files = list_files(folder_id)
        
        if not files:
            console.print("[yellow]Empty folder[/yellow]")
            return
        
        # Create table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Type", style="dim", width=6)
        table.add_column("Name")
        table.add_column("Size", justify="right")
        table.add_column("Modified", style="dim")
        
        for file in files:
            file_type = "📁 DIR" if is_folder(file) else "📄 FILE"
            name = file['name']
            size = format_size(file.get('size'))
            modified = file.get('modifiedTime', 'Unknown')[:10]  # Just the date part
            
            table.add_row(file_type, name, size, modified)
        
        console.print(table)
        console.print(f"\n[dim]{len(files)} items[/dim]")
        
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
