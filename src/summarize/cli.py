import logging
import sys

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from summarize.extractor import extract
from summarize.summarizer import summarize

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

console = Console()


def main() -> None:
    if len(sys.argv) < 2:
        console.print("[red]Uso:[/red] summarize <url ou caminho-do-pdf>")
        sys.exit(1)

    source = sys.argv[1]

    with console.status("[bold]Extraindo texto...[/bold]"):
        try:
            text = extract(source)
        except (RuntimeError, FileNotFoundError) as e:
            console.print(f"[red]Erro:[/red] {e}")
            sys.exit(1)

    with console.status("[bold]Resumindo com Gemini...[/bold]"):
        try:
            summary = summarize(text)
        except ValueError as e:
            console.print(f"[red]Erro:[/red] {e}")
            sys.exit(1)

    console.print(Panel(Markdown(summary), title="Resumo", border_style="bright_black"))


if __name__ == "__main__":
    main()