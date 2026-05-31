import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

MAX_CHARS = 30_000  # limite de texto enviado ao Gemini
TIMEOUT = 20.0

if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY não encontrada. Configure o arquivo .env")
