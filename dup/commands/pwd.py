"""Print working directory command."""

import typer
from rich.console import Console
from ..config import get_current_path

console = Console()


def pwd_command():
    """Show current Drive path."""
    try:
        current_path = get_current_path()
        console.print(f"[cyan]{current_path}[/cyan]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)
