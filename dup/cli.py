"""Main CLI entry point for DUP."""

import typer
from rich.console import Console
from typing import Optional
from . import __version__
from .auth import authenticate, is_authenticated, get_drive_service
from .commands.ls import ls_command
from .commands.tree import tree_command
from .commands.cd import cd_command
from .commands.pwd import pwd_command
from .commands.upload import upload_command
from .commands.link import link_command
from .commands.download import download_command

app = typer.Typer(
    name="dup",
    help="Drive Upload Program - Manage Google Drive from the command line",
    add_completion=False
)
console = Console()


@app.command()
def login():
    """Authenticate with Google Drive."""
    try:
        if is_authenticated():
            console.print("[yellow]Already authenticated![/yellow]")
            console.print("Re-authenticating...")
        
        with console.status("[bold green]Opening browser for authentication..."):
            service = get_drive_service()
        
        # Test the connection
        service.files().list(pageSize=1).execute()
        
        console.print("[green]✓ Successfully authenticated with Google Drive![/green]")
        
    except Exception as e:
        console.print(f"[red]Authentication failed:[/red] {str(e)}")
        raise typer.Exit(1)


@app.command()
def ls(path: Optional[str] = typer.Argument(None, help="Path to list (optional)")):
    """List files in current or specified Drive folder."""
    ls_command(path)


@app.command()
def tree(path: Optional[str] = typer.Argument(None, help="Path to show tree for (optional)")):
    """Show recursive folder structure."""
    tree_command(path)


@app.command()
def cd(path: str = typer.Argument(..., help="Path to change to")):
    """Change current Drive folder."""
    cd_command(path)


@app.command()
def pwd():
    """Show current Drive path."""
    pwd_command()


@app.command()
def up(path: str = typer.Argument(..., help="Local file or folder to upload")):
    """Upload file or folder to current Drive location."""
    upload_command(path)


@app.command()
def link(name: str = typer.Argument(..., help="File name to get link for")):
    """Generate shareable Google Drive link for a file."""
    link_command(name)


@app.command()
def down(
    filename: str = typer.Argument(..., help="File name to download"),
    destination: str = typer.Option(".", "--dest", "-d", help="Download destination (default: current directory)")
):
    """Download a file from current Drive location."""
    download_command(filename, destination)


@app.command()
def version():
    """Show version information."""
    console.print(f"[cyan]dup[/cyan] version [green]{__version__}[/green]")


@app.callback()
def main(
    ctx: typer.Context,
    version_flag: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version information",
        is_eager=True
    )
):
    """
    DUP - Drive Upload Program
    
    Manage Google Drive files from the command line.
    """
    if version_flag:
        console.print(f"[cyan]dup[/cyan] version [green]{__version__}[/green]")
        raise typer.Exit()
    
    # Check if user is authenticated for commands that need it
    if ctx.invoked_subcommand and ctx.invoked_subcommand != 'login':
        if not is_authenticated():
            console.print("[yellow]⚠️  Not authenticated with Google Drive[/yellow]")
            console.print("Run [cyan]dup login[/cyan] to authenticate")
            raise typer.Exit(1)


def cli():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    cli()
