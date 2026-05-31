import logging

from google import genai

from summarize.config import GEMINI_API_KEY, GEMINI_MODEL

log = logging.getLogger(__name__)

client = genai.Client(api_key=GEMINI_API_KEY)

PROMPT = """
Você é um especialista em síntese e análise de textos.

Sua tarefa é ler o texto fornecido e produzir uma resposta estruturada em português.

Regras:
- Seja objetivo, claro e fiel ao conteúdo original.
- Não invente informações nem faça inferências sem base no texto.
- Evite repetições.
- Use linguagem simples e profissional.
- Caso o texto seja muito curto, adapte o resumo sem repetir frases literalmente.

Formato da resposta:

## Resumo
(Até 5 frases)

## Principais pontos
- Ponto 1
- Ponto 2
- Ponto 3

## Conclusão
(Uma única frase que sintetize a ideia central)

Texto:
{text}
"""


def summarize(text: str) -> str:
    if not text.strip():
        raise ValueError("Texto vazio — nada para resumir.")

    log.info("Enviando %d caracteres para o Gemini...", len(text))

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT.format(text=text),
    )
    return response.text
