import logging
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from pypdf import PdfReader

from summarize.config import MAX_CHARS, TIMEOUT

log = logging.getLogger(__name__)


def from_url(url: str) -> str:
    log.info("Extraindo texto de URL: %s", url)
    try:
        response = httpx.get(url, timeout=TIMEOUT, follow_redirects=True)
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"HTTP {e.response.status_code} ao acessar {url}") from e
    except httpx.RequestError as e:
        raise RuntimeError(f"Erro de conexão: {e}") from e

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove ruído
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    log.info("Extraídos %d caracteres da URL", len(text))
    return text[:MAX_CHARS]


def from_pdf(path: str | Path) -> str:
    path = Path(path)
    log.info("Extraindo texto do PDF: %s", path)

    if not path.exists():
        raise FileNotFoundError(f"PDF não encontrado: {path}")

    reader = PdfReader(str(path))
    pages  = [page.extract_text() or "" for page in reader.pages]
    text   = "\n".join(pages)

    log.info("Extraídos %d caracteres do PDF (%d páginas)", len(text), len(reader.pages))
    return text[:MAX_CHARS]


def extract(source: str) -> str:
    """Detecta automaticamente se é URL ou caminho de PDF."""
    if source.startswith("http://") or source.startswith("https://"):
        return from_url(source)
    return from_pdf(source)