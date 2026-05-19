import re
import pytest
from pathlib import Path

HTML_FILE = Path(__file__).parent / "index.html"


@pytest.fixture(scope="module")
def html():
    return HTML_FILE.read_text(encoding="utf-8")


# ── File existence ────────────────────────────────────────────────────────────

def test_index_html_exists():
    assert HTML_FILE.exists(), "index.html must exist"


# ── Document structure ────────────────────────────────────────────────────────

def test_doctype(html):
    assert html.strip().lower().startswith("<!doctype html>")

def test_html_lang_en(html):
    assert re.search(r'<html[^>]+lang=["\']en["\']', html, re.IGNORECASE)

def test_meta_charset_utf8(html):
    assert re.search(r'<meta[^>]+charset=["\']?UTF-8["\']?', html, re.IGNORECASE)

def test_viewport_meta(html):
    assert re.search(r'<meta[^>]+name=["\']viewport["\']', html, re.IGNORECASE)

def test_title_weather_app(html):
    assert re.search(r'<title>\s*Weather App\s*</title>', html, re.IGNORECASE)

# ... (all remaining tests unchanged) ...

def test_search_button_disabled_while_loading(html):
    assert re.search(r'searchBtn.*disabled|disabled.*searchBtn', html, re.DOTALL)