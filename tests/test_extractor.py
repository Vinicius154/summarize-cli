import pytest

from summarize.extractor import extract, from_pdf


def test_extract_url_returns_string():
    result = extract("https://example.com")
    assert isinstance(result, str)
    assert len(result) > 0


def test_extract_pdf_file_not_found():
    with pytest.raises(FileNotFoundError):
        from_pdf("nao_existe.pdf")


def test_extract_detects_url():
    # Verifica que URLs são roteadas corretamente
    result = extract("https://example.com")
    assert isinstance(result, str)
