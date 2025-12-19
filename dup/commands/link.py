"""Generate shareable link command."""

import typer
from rich.console import Console
from ..drive import get_file_by_name, get_file_link, make_file_public, is_file_public, resolve_path
from ..config import get_current_folder_id

console = Console()


def link_command(name: str):
    """Generate shareable Google Drive link for a file."""
    try:
        folder_id = get_current_folder_id()
        
        # Try to find the file by name
        file = get_file_by_name(name, folder_id)
        
        if not file:
            console.print(f"[red]Error:[/red] File not found: {name}")
            raise typer.Exit(1)
        
        file_id = file['id']
        
        # Check if file is already public
        if is_file_public(file_id):
            link = get_file_link(file_id)
            console.print(f"[green]📎 Link:[/green] {link}")
        else:
            # Ask for confirmation to make public
            console.print(f"[yellow]⚠️  File '{name}' is private.[/yellow]")
            make_public = typer.confirm("Make it publicly accessible?")
            
            if make_public:
                make_file_public(file_id)
                link = get_file_link(file_id)
                console.print(f"[green]✓ File is now public[/green]")
                console.print(f"[green]📎 Link:[/green] {link}")
            else:
                console.print("[yellow]File remains private. Getting link anyway...[/yellow]")
                link = get_file_link(file_id)
                console.print(f"[dim]📎 Link (requires access):[/dim] {link}")
        
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
