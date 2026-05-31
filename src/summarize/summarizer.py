import logging

import google.generativeai as genai

from summarize.config import GEMINI_API_KEY, GEMINI_MODEL

log = logging.getLogger(__name__)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

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
        raise ValueError("Texto vazio, nada para resumir.")

    log.info("Enviando %d caracteres para o Gemini...", len(text))

    response = model.generate_content(PROMPT.format(text=text))
    return response.text