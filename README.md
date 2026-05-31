# summarize-cli

CLI que resume qualquer URL ou PDF usando Gemini.
Uma linha de comando, resultado em segundos.

## Uso

```bash
summarize https://site.com/artigo
summarize documento.pdf
```

## Setup

```bash
git clone https://github.com/Vinicius154/summarize-cli
cd summarize-cli

# instala uv se não tiver
curl -LsSf https://astral.sh/uv/install.sh | sh

uv pip install -e .

# cria o .env com sua chave
echo "GEMINI_API_KEY=sua_chave" > .env
# chave gratuita em: https://aistudio.google.com/app/apikey
# chave recomendada: gemini-2.5-flash

summarize https://exemplo.com/artigo
```

## Stack

Python 3.13 · uv · httpx · BeautifulSoup · pypdf · Gemini · rich
