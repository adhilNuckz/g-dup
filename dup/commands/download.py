"""Download file command."""

import os
import typer
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from ..drive import get_file_by_name, download_file, is_folder
from ..config import get_current_folder_id

console = Console()


def download_command(filename: str, destination: str = "."):
    """Download a file from current Drive location to local machine."""
    try:
        folder_id = get_current_folder_id()
        
        # Find the file
        file = get_file_by_name(filename, folder_id)
        
        if not file:
            console.print(f"[red]Error:[/red] File not found: {filename}")
            raise typer.Exit(1)
        
        # Check if it's a folder
        if is_folder(file):
            console.print(f"[red]Error:[/red] Cannot download folders yet. '{filename}' is a folder.")
            console.print("[yellow]Tip:[/yellow] Use 'dup down <filename>' for individual files only.")
            raise typer.Exit(1)
        
        file_id = file['id']
        
        # Prepare destination path
        dest_path = Path(destination)
        if dest_path.is_dir():
            # If destination is a directory, save file with its original name
            dest_file = dest_path / filename
        else:
            # If destination is a file path, use it directly
            dest_file = dest_path
        
        # Ensure parent directory exists
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Download with progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            console=console
        ) as progress:
            task = progress.add_task(f"Downloading {filename}", total=100)
            
            def callback(progress_val):
                progress.update(task, completed=progress_val * 100)
            
            result_path = download_file(file_id, str(dest_file), callback)
            progress.update(task, completed=100)
        
        console.print(f"[green]✓ Downloaded:[/green] {filename}")
        console.print(f"[dim]Saved to: {result_path}[/dim]")
        
    except FileNotFoundError as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
    except ValueError as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
