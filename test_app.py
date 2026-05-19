import re
import pytest
from pathlib import Path

HTML_FILE = Path(__file__).parent / "index.html"

@pytest.fixture(scope="module")
def html():
    return HTML_FILE.read_text(encoding="utf-8")


# ── Structure ──────────────────────────────────────────────────────────────────

def test_html_file_exists():
    assert HTML_FILE.exists(), "index.html not found"

def test_doctype(html):
    assert html.strip().startswith("<!DOCTYPE html>")

def test_lang_attribute(html):
    assert 'lang="en"' in html

def test_charset_utf8(html):
    assert re.search(r'<meta\s+charset=["\']UTF-8["\']', html, re.IGNORECASE)

def test_viewport_meta(html):
    assert re.search(r'<meta\s+name=["\']viewport["\']', html, re.IGNORECASE)

def test_title(html):
    assert re.search(r'<title>\s*Weather App\s*</title>', html)


# ── Required IDs ──────────────────────────────────────────────────────────────

@pytest.mark.parametrize("element_id", [
    "cityInput", "searchBtn", "errorMsg", "spinner", "card",
    "cityName", "countryName", "weatherIcon", "condition",
    "temperature", "unitToggle", "celsiusBtn", "fahrenheitBtn",
    "humidity", "windSpeed",
])
def test_required_id_present(html, element_id):
    assert f'id="{element_id}"' in html, f'Missing id="{element_id}"'

# ... (all remaining tests unchanged) ...

def test_details_labels_present(html):
    assert "Humidity" in html
    assert "Wind Speed" in html