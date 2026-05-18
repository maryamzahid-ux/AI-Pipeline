import re
from pathlib import Path

HTML = Path("index.html").read_text(encoding="utf-8")


# --- Structure tests ---

def test_html_has_doctype():
    assert HTML.strip().lower().startswith("<!doctype html>")


def test_page_title():
    assert re.search(r"<title>\s*Weather App\s*</title>", HTML, re.IGNORECASE)


def test_h1_heading():
    assert re.search(r"<h1[^>]*>\s*Weather App\s*</h1>", HTML, re.IGNORECASE)


def test_city_input_present():
    assert re.search(r'id=["\']cityInput["\']', HTML)


def test_search_button_present():
    assert re.search(r'id=["\']searchBtn["\']', HTML)


def test_unit_toggle_buttons_present():
    assert re.search(r'id=["\']btnC["\']', HTML)
    assert re.search(r'id=["\']btnF["\']', HTML)


def test_celsius_button_active_by_default():
    match = re.search(r'id=["\']btnC["\'][^>]*class=["\'][^"\']*active', HTML)
    if not match:
        match = re.search(r'class=["\'][^"\']*active[^"\']*["\'][^>]*id=["\']btnC["\']', HTML)
    assert match, "btnC should have 'active' class by default"


def test_weather_card_present():
    assert re.search(r'id=["\']weatherCard["\']', HTML)


def test_weather_card_hidden_by_default():
    card_match = re.search(r'<div[^>]+id=["\']weatherCard["\'][^>]*>', HTML)
    assert card_match
    tag = card_match.group(0)
    # card element should not have 'visible' class in markup
    assert "visible" not in tag


def test_loading_element_present():
    assert re.search(r'id=["\']loading["\']', HTML)


def test_error_msg_element_present():
    assert re.search(r'id=["\']errorMsg["\']', HTML)


def test_weather_emoji_element():
    assert re.search(r'id=["\']weatherEmoji["\']', HTML)


def test_temp_main_element():
    assert re.search(r'id=["\']tempMain["\']', HTML)


def test_condition_label_element():
    assert re.search(r'id=["\']conditionLabel["\']', HTML)


def test_city_label_element():
    assert re.search(r'id=["\']cityLabel["\']', HTML)


def test_humidity_element():
    assert re.search(r'id=["\']humidity["\']', HTML)


def test_wind_speed_element():
    assert re.search(r'id=["\']windSpeed["\']', HTML)


def test_spinner_element():
    assert re.search(r'class=["\']spinner["\']', HTML)


# --- CSS tests ---

def test_card_hidden_by_default_css():
    # .card should have display:none
    card_rule = re.search(r'\.card\s*\{[^}]+\}', HTML, re.DOTALL)
    assert card_rule
    assert "display: none" in card_rule.group(0) or "display:none" in card_rule.group(0)


def test_card_visible_css():
    assert re.search(r'\.card\.visible\s*\{[^}]*display\s*:\s*block', HTML, re.DOTALL)


def test_error_msg_hidden_by_default_css():
    err_rule = re.search(r'\.error-msg\s*\{[^}]+\}', HTML, re.DOTALL)
    assert err_rule
    assert "display: none" in err_rule.group(0) or "display:none" in err_rule.group(0)


def test_error_msg_visible_css():
    assert re.search(r'\.error-msg\.visible\s*\{[^}]*display\s*:\s*block', HTML, re.DOTALL)


def test_loading_hidden_by_default_css():
    loading_rule = re.search(r'\.loading\s*\{[^}]+\}', HTML, re.DOTALL)
    assert loading_rule
    assert "display: none" in loading_rule.group(0) or "display:none" in loading_rule.group(0)


def test_spin_keyframes_defined():
    assert re.search(r'@keyframes\s+spin', HTML)


def test_active_button_style():
    assert re.search(r'\.unit-toggle\s+button\.active\s*\{[^}]*background\s*:', HTML, re.DOTALL)


# --- JavaScript logic tests ---

def test_wmo_codes_defined():
    assert "const WMO" in HTML or "var WMO" in HTML or "let WMO" in HTML


def test_wmo_clear_sky_entry():
    assert "'Clear Sky'" in HTML or '"Clear Sky"' in HTML


def test_wmo_thunderstorm_entry():
    assert "'Thunderstorm'" in HTML or '"Thunderstorm"' in HTML


def test_ctof_conversion_function():
    assert re.search(r'function\s+cToF', HTML)


def test_ctof_formula_correct():
    # formula: c * 9 / 5 + 32
    assert re.search(r'c\s*\*\s*9\s*/\s*5\s*\+\s*32', HTML)


def test_get_wmo_function():
    assert re.search(r'function\s+getWMO', HTML)


def test_get_wmo_fallback():
    # unknown codes should return a fallback
    assert re.search(r"label\s*:\s*['\"]Unknown['\"]", HTML)


def test_state_object_defined():
    assert re.search(r"let\s+state\s*=\s*\{", HTML)


def test_state_has_unit():
    assert re.search(r"unit\s*:\s*['\"]C['\"]", HTML)


def test_render_card_function():
    assert re.search(r'function\s+renderCard', HTML)


def test_fetch_weather_function():
    assert re.search(r'(async\s+function\s+fetchWeather|fetchWeather\s*=\s*async)', HTML)


def test_geocoding_api_url():
    assert "geocoding-api.open-meteo.com/v1/search" in HTML


def test_weather_api_url():
    assert "api.open-meteo.com/v1/forecast" in HTML


def test_encode_uri_city():
    assert "encodeURIComponent" in HTML


def test_city_not_found_error_message():
    assert "not found" in HTML


def test_local_storage_save():
    assert "localStorage.setItem" in HTML
    assert "'lastCity'" in HTML or '"lastCity"' in HTML


def test_local_storage_restore():
    assert "localStorage.getItem" in HTML


def test_search_button_click_listener():
    assert re.search(r"searchBtn\.addEventListener\s*\(\s*['\"]click['\"]", HTML)


def test_enter_key_listener():
    assert re.search(r"['\"]keydown['\"]", HTML)
    assert re.search(r"['\"]Enter['\"]", HTML)


def test_unit_toggle_c_listener():
    assert re.search(r"btnC\.addEventListener\s*\(\s*['\"]click['\"]", HTML)


def test_unit_toggle_f_listener():
    assert re.search(r"btnF\.addEventListener\s*\(\s*['\"]click['\"]", HTML)


def test_celsius_display_format():
    # temperature rendered as e.g. "25°C"
    assert "°C`" in HTML or "°C'" in HTML or '°C"' in HTML or "°C}" in HTML


def test_fahrenheit_display_format():
    assert "°F`" in HTML or "°F'" in HTML or '°F"' in HTML or "°F}" in HTML


def test_humidity_percent_display():
    assert '${state.humidity}%' in HTML or "{state.humidity}%" in HTML


def test_wind_speed_kmh_display():
    assert "km/h" in HTML


# --- Accessibility / meta tests ---

def test_charset_utf8():
    assert re.search(r'charset=["\']UTF-8["\']', HTML, re.IGNORECASE)


def test_viewport_meta():
    assert re.search(r'name=["\']viewport["\']', HTML, re.IGNORECASE)


def test_lang_attribute():
    assert re.search(r'<html[^>]+lang=["\']en["\']', HTML, re.IGNORECASE)


def test_input_autocomplete_off():
    assert re.search(r'autocomplete=["\']off["\']', HTML, re.IGNORECASE)


def test_responsive_media_query():
    assert re.search(r'@media\s*\(max-width\s*:\s*375px\)', HTML)