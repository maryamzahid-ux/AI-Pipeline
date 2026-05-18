import re
import pytest
from pathlib import Path

HTML_FILE = Path(__file__).parent / "index.html"

@pytest.fixture(scope="module")
def html():
    return HTML_FILE.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# File / basic structure
# ---------------------------------------------------------------------------

def test_file_exists():
    assert HTML_FILE.exists(), "index.html not found"

def test_doctype(html):
    assert html.strip().startswith("<!DOCTYPE html>")

def test_html_lang_en(html):
    assert re.search(r'<html[^>]+lang=["\']en["\']', html)

def test_charset_utf8(html):
    assert re.search(r'<meta[^>]+charset=["\']?UTF-8["\']?', html, re.IGNORECASE)

def test_viewport_meta(html):
    assert re.search(r'<meta[^>]+name=["\']viewport["\']', html)

def test_title_weather_app(html):
    assert re.search(r'<title>\s*Weather App\s*</title>', html)


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

def test_header_exists(html):
    assert '<header>' in html

def test_h1_text(html):
    assert re.search(r'<h1>\s*Weather\s*</h1>', html)

def test_header_subtitle(html):
    assert re.search(r'<p>\s*Live conditions for any city\s*</p>', html)


# ---------------------------------------------------------------------------
# Search bar
# ---------------------------------------------------------------------------

def test_search_bar_div(html):
    assert re.search(r'<div[^>]+class=["\']search-bar["\']', html)

def test_city_input_exists(html):
    assert re.search(r'<input[^>]+id=["\']cityInput["\']', html)

def test_city_input_type_text(html):
    assert re.search(r'<input[^>]+type=["\']text["\']', html)

def test_city_input_placeholder(html):
    assert re.search(r'placeholder=["\']Enter city name', html)

def test_city_input_autocomplete_off(html):
    assert re.search(r'<input[^>]+id=["\']cityInput["\'][^>]*autocomplete=["\']off["\']'
                     r'|autocomplete=["\']off["\'][^>]*id=["\']cityInput["\']', html)

def test_search_button_exists(html):
    assert re.search(r'<button[^>]+id=["\']searchBtn["\']', html)

def test_search_button_text(html):
    assert re.search(r'id=["\']searchBtn["\'][^>]*>\s*Search\s*</button>'
                     r'|<button[^>]*id=["\']searchBtn["\'][^>]*>\s*Search', html)


# ---------------------------------------------------------------------------
# Error message & spinner
# ---------------------------------------------------------------------------

def test_error_msg_element(html):
    assert re.search(r'id=["\']errorMsg["\']', html)

def test_error_msg_class(html):
    assert re.search(r'class=["\']error-msg["\']', html)

def test_spinner_element(html):
    assert re.search(r'id=["\']spinner["\']', html)

def test_spinner_class(html):
    assert re.search(r'class=["\']spinner["\']', html)


# ---------------------------------------------------------------------------
# Weather card
# ---------------------------------------------------------------------------

def test_card_element(html):
    assert re.search(r'<div[^>]+class=["\']card["\'][^>]*id=["\']card["\']'
                     r'|<div[^>]+id=["\']card["\'][^>]*class=["\']card["\']', html)

def test_card_top_div(html):
    assert re.search(r'class=["\']card-top["\']', html)

def test_city_name_element(html):
    assert re.search(r'id=["\']cityName["\']', html)

def test_country_name_element(html):
    assert re.search(r'id=["\']countryName["\']', html)

def test_weather_icon_element(html):
    assert re.search(r'id=["\']weatherIcon["\']', html)

def test_condition_element(html):
    assert re.search(r'id=["\']condition["\']', html)

def test_temperature_row(html):
    assert re.search(r'class=["\']temperature-row["\']', html)

def test_temperature_element(html):
    assert re.search(r'id=["\']temperature["\']', html)

def test_unit_toggle_button(html):
    assert re.search(r'id=["\']unitToggle["\']', html)

def test_unit_toggle_aria_label(html):
    assert re.search(r'aria-label=["\']Toggle temperature unit["\']', html)

def test_celsius_btn(html):
    assert re.search(r'id=["\']celsiusBtn["\']', html)

def test_celsius_btn_active_by_default(html):
    assert re.search(r'id=["\']celsiusBtn["\'][^>]*class=["\'][^"\']*active[^"\']*["\']'
                     r'|class=["\'][^"\']*active[^"\']*["\'][^>]*id=["\']celsiusBtn["\']', html)

def test_fahrenheit_btn(html):
    assert re.search(r'id=["\']fahrenheitBtn["\']', html)

def test_celsius_label(html):
    assert '°C' in html

def test_fahrenheit_label(html):
    assert '°F' in html


# ---------------------------------------------------------------------------
# Details section
# ---------------------------------------------------------------------------

def test_details_div(html):
    assert re.search(r'class=["\']details["\']', html)

def test_humidity_label(html):
    assert re.search(r'Humidity', html)

def test_humidity_element(html):
    assert re.search(r'id=["\']humidity["\']', html)

def test_wind_speed_label(html):
    assert re.search(r'Wind Speed', html)

def test_wind_speed_element(html):
    assert re.search(r'id=["\']windSpeed["\']', html)

def test_detail_items_count(html):
    items = re.findall(r'class=["\']detail-item["\']', html)
    assert len(items) == 2


# ---------------------------------------------------------------------------
# CSS: variables and key rules
# ---------------------------------------------------------------------------

def test_css_variable_bg(html):
    assert '--bg:' in html or '--bg :' in html

def test_css_variable_accent(html):
    assert '--accent:' in html

def test_css_variable_radius(html):
    assert '--radius:' in html

def test_card_hidden_by_default(html):
    # .card { display: none } before .card.visible overrides it
    assert re.search(r'\.card\s*\{[^}]*display\s*:\s*none', html, re.DOTALL)

def test_card_visible_class(html):
    assert re.search(r'\.card\.visible\s*\{[^}]*display\s*:\s*block', html, re.DOTALL)

def test_error_msg_hidden_by_default(html):
    assert re.search(r'\.error-msg\s*\{[^}]*display\s*:\s*none', html, re.DOTALL)

def test_error_msg_visible_class(html):
    assert re.search(r'\.error-msg\.visible\s*\{[^}]*display\s*:\s*block', html, re.DOTALL)

def test_spinner_hidden_by_default(html):
    assert re.search(r'\.spinner\s*\{[^}]*display\s*:\s*none', html, re.DOTALL)

def test_spinner_visible_class(html):
    assert re.search(r'\.spinner\.visible\s*\{[^}]*display\s*:\s*block', html, re.DOTALL)

def test_spin_keyframe(html):
    assert re.search(r'@keyframes\s+spin', html)

def test_responsive_media_query(html):
    assert re.search(r'@media\s*\([^)]*max-width\s*:\s*400px\s*\)', html)


# ---------------------------------------------------------------------------
# JavaScript: logic and constants
# ---------------------------------------------------------------------------

def test_storage_key_constant(html):
    assert "STORAGE_KEY" in html
    assert re.search(r"STORAGE_KEY\s*=\s*['\"]weather_last_city['\"]", html)

def test_wmo_codes_object(html):
    assert "WMO_CODES" in html

def test_wmo_code_clear_sky(html):
    assert re.search(r"0\s*:\s*\{[^}]*Clear Sky", html)

def test_wmo_code_thunderstorm(html):
    assert re.search(r"95\s*:\s*\{[^}]*Thunderstorm", html)

def test_wmo_codes_coverage(html):
    # At least 20 WMO code entries
    entries = re.findall(r'\d+\s*:\s*\{[^}]*label', html)
    assert len(entries) >= 20

def test_to_fahrenheit_formula(html):
    # toF must implement c * 9 / 5 + 32
    assert re.search(r'c\s*\*\s*9\s*/\s*5\s*\+\s*32', html)

def test_render_temperature_function(html):
    assert 'renderTemperature' in html

def test_geocode_function(html):
    assert 'async function geocode' in html

def test_fetch_weather_function(html):
    assert 'async function fetchWeather' in html

def test_display_weather_function(html):
    assert 'function displayWeather' in html

def test_search_function(html):
    assert 'async function search' in html

def test_geocoding_api_url(html):
    assert 'geocoding-api.open-meteo.com' in html

def test_weather_api_url(html):
    assert 'api.open-meteo.com/v1/forecast' in html

def test_geocode_uses_encode_uri(html):
    assert 'encodeURIComponent' in html

def test_weather_api_params(html):
    assert 'temperature_2m' in html
    assert 'relative_humidity_2m' in html
    assert 'wind_speed_10m' in html
    assert 'weather_code' in html

def test_local_storage_set(html):
    assert re.search(r'localStorage\.setItem\s*\(\s*STORAGE_KEY', html)

def test_local_storage_get(html):
    assert re.search(r'localStorage\.getItem\s*\(\s*STORAGE_KEY', html)

def test_search_btn_click_listener(html):
    assert re.search(r"['\"]click['\"]", html)

def test_enter_key_listener(html):
    assert re.search(r"['\"]keydown['\"]", html)
    assert re.search(r"['\"]Enter['\"]", html)

def test_unit_toggle_click_listener(html):
    assert re.search(r'unitToggle.*addEventListener|addEventListener.*unitToggle', html, re.DOTALL)

def test_unit_toggle_logic(html):
    # Toggling flips between 'C' and 'F'
    assert re.search(r"unit\s*===\s*['\"]C['\"].*['\"]F['\"]|['\"]F['\"].*unit\s*===\s*['\"]C['\"]",
                     html, re.DOTALL)

def test_set_loading_disables_button(html):
    assert re.search(r'searchBtn.*disabled|disabled.*searchBtn', html, re.DOTALL)

def test_error_shown_on_failure(html):
    assert 'showError' in html
    assert re.search(r'catch\s*\(', html)

def test_clear_error_called_on_search(html):
    assert 'clearError' in html

def test_loading_finally_block(html):
    assert 'finally' in html
    assert re.search(r'finally\s*\{[^}]*setLoading\s*\(\s*false\s*\)', html, re.DOTALL)

def test_state_object(html):
    assert re.search(r'let\s+state\s*=\s*\{', html)
    assert re.search(r'tempC\s*:\s*null', html)
    assert re.search(r"unit\s*:\s*['\"]C['\"]", html)

def test_last_city_auto_search(html):
    # On load, if lastCity exists in localStorage, it is searched automatically
    assert re.search(r'if\s*\(\s*lastCity\s*\)', html)
    assert re.search(r'search\s*\(\s*lastCity\s*\)', html)

def test_city_input_value_restored(html):
    assert re.search(r"cityInput.*\.value\s*=\s*lastCity|value\s*=\s*lastCity.*cityInput",
                     html, re.DOTALL)