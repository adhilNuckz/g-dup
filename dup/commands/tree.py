"""Tree view command."""

import typer
from rich.console import Console
from rich.tree import Tree as RichTree
from ..drive import list_files, is_folder, build_tree
from ..config import get_current_folder_id, get_current_path

console = Console()


def tree_command(path: str = None):
    """Show recursive folder structure."""
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
        
        console.print(f"[cyan]📂 {current_path}[/cyan]")
        
        # Build tree
        tree_lines = build_tree(folder_id)
        
        if not tree_lines:
            console.print("[yellow]Empty folder[/yellow]")
            return
        
        for line in tree_lines:
            console.print(line)
        
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
