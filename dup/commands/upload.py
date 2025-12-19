"""Upload file or folder command."""

import os
import typer
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from ..drive import upload_file, upload_folder, get_file_by_id
from ..config import get_current_folder_id

console = Console()


def upload_command(path: str):
    """Upload file or folder to current Drive location."""
    try:
        # Check if path exists
        local_path = Path(path)
        if not local_path.exists():
            console.print(f"[red]Error:[/red] Path not found: {path}")
            raise typer.Exit(1)
        
        folder_id = get_current_folder_id()
        
        if local_path.is_file():
            # Upload single file
            file_size = local_path.stat().st_size
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeRemainingColumn(),
                console=console
            ) as progress:
                task = progress.add_task(f"Uploading {local_path.name}", total=100)
                
                def callback(progress_val):
                    progress.update(task, completed=progress_val * 100)
                
                result = upload_file(str(local_path), folder_id, callback)
                progress.update(task, completed=100)
            
            console.print(f"[green]✓ Uploaded:[/green] {result['name']}")
            console.print(f"[dim]Link: {result.get('webViewLink', 'N/A')}[/dim]")
            
        elif local_path.is_dir():
            # Upload folder
            console.print(f"[cyan]Uploading folder:[/cyan] {local_path.name}")
            
            with console.status("[bold green]Uploading files..."):
                result = upload_folder(str(local_path), folder_id)
            
            console.print(f"[green]✓ Uploaded folder:[/green] {result['name']}")
        
        else:
            console.print(f"[red]Error:[/red] Invalid path type")
            raise typer.Exit(1)
            
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
