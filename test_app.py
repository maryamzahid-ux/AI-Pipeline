import re
import pytest
from pathlib import Path

HTML = Path(__file__).parent / "index.html"

@pytest.fixture(scope="module")
def html():
    return HTML.read_text(encoding="utf-8")


# --- Structure ---

def test_html_file_exists():
    assert HTML.exists()

def test_doctype(html):
    assert html.strip().lower().startswith("<!doctype html>")

def test_lang_attribute(html):
    assert re.search(r'<html[^>]+lang=["\']en["\']', html)

def test_charset_utf8(html):
    assert re.search(r'<meta[^>]+charset=["\']?UTF-8["\']?', html, re.IGNORECASE)

def test_viewport_meta(html):
    assert re.search(r'<meta[^>]+name=["\']viewport["\']', html)

def test_title_weather(html):
    assert re.search(r'<title>\s*Weather App\s*</title>', html)


# --- Header ---

def test_header_h1_text(html):
    assert re.search(r'<h1[^>]*>\s*Weather\s*</h1>', html)

def test_header_subtitle(html):
    assert re.search(r'<p[^>]*>\s*Live conditions for any city\s*</p>', html)


# --- Search bar ---

def test_city_input_exists(html):
    assert re.search(r'<input[^>]+id=["\']cityInput["\']', html)

def test_city_input_type_text(html):
    assert re.search(r'<input[^>]+id=["\']cityInput["\'][^>]*type=["\']text["\']|<input[^>]+type=["\']text["\'][^>]*id=["\']cityInput["\']', html)

def test_city_input_placeholder(html):
    assert re.search(r'placeholder=["\']Enter city name', html)

def test_search_button_exists(html):
    assert re.search(r'<button[^>]+id=["\']searchBtn["\']', html)

def test_search_button_text(html):
    assert re.search(r'id=["\']searchBtn["\'][^>]*>\s*Search\s*</button>|>\s*Search\s*</button>', html)


# --- Error / Spinner / Card elements ---

def test_error_msg_div_exists(html):
    assert re.search(r'<div[^>]+id=["\']errorMsg["\']', html)

def test_error_msg_hidden_by_default(html):
    match = re.search(r'<div[^>]+id=["\']errorMsg["\'][^>]*class=["\']([^"\']*)["\']|class=["\']([^"\']*)["\'][^>]*id=["\']errorMsg["\']', html)
    # The element has class "error-msg" (no "visible"), meaning it's hidden by default via CSS
    assert re.search(r'class=["\']error-msg["\']', html)

def test_spinner_div_exists(html):
    assert re.search(r'<div[^>]+id=["\']spinner["\']', html)

def test_card_div_exists(html):
    assert re.search(r'<div[^>]+id=["\']card["\']', html)

def test_card_hidden_by_default(html):
    # card div should NOT have "visible" class in source HTML
    match = re.search(r'<div[^>]+id=["\']card["\'][^>]*>', html)
    assert match
    assert "visible" not in match.group(0)


# --- Card content elements ---

def test_city_name_element(html):
    assert re.search(r'id=["\']cityName["\']', html)

def test_country_name_element(html):
    assert re.search(r'id=["\']countryName["\']', html)

def test_weather_icon_element(html):
    assert re.search(r'id=["\']weatherIcon["\']', html)

def test_condition_element(html):
    assert re.search(r'id=["\']condition["\']', html)

def test_temperature_element(html):
    assert re.search(r'id=["\']temperature["\']', html)

def test_humidity_element(html):
    assert re.search(r'id=["\']humidity["\']', html)

def test_wind_speed_element(html):
    assert re.search(r'id=["\']windSpeed["\']', html)


# --- Unit toggle ---

def test_unit_toggle_button_exists(html):
    assert re.search(r'<button[^>]+id=["\']unitToggle["\']', html)

def test_unit_toggle_aria_label(html):
    assert re.search(r'aria-label=["\']Toggle temperature unit["\']', html)

def test_celsius_btn_exists(html):
    assert re.search(r'id=["\']celsiusBtn["\']', html)

def test_fahrenheit_btn_exists(html):
    assert re.search(r'id=["\']fahrenheitBtn["\']', html)

def test_celsius_active_by_default(html):
    match = re.search(r'<span[^>]+id=["\']celsiusBtn["\'][^>]*class=["\']([^"\']*)["\']|<span[^>]+class=["\']([^"\']*)["\'][^>]*id=["\']celsiusBtn["\']', html)
    assert match
    classes = match.group(1) or match.group(2)
    assert "active" in classes

def test_fahrenheit_not_active_by_default(html):
    match = re.search(r'<span[^>]+id=["\']fahrenheitBtn["\'][^>]*>|<span[^>]+class=["\']([^"\']*)["\'][^>]*id=["\']fahrenheitBtn["\']', html)
    assert match


# --- CSS variables ---

def test_css_custom_properties(html):
    assert "--bg:" in html
    assert "--accent:" in html
    assert "--text:" in html
    assert "--surface:" in html

def test_css_spin_keyframe(html):
    assert re.search(r'@keyframes\s+spin', html)

def test_spinner_animation(html):
    assert re.search(r'animation:\s*spin', html)

def test_media_query_responsive(html):
    assert re.search(r'@media\s*\(max-width:\s*400px\)', html)


# --- JavaScript ---

def test_script_tag_present(html):
    assert "<script>" in html or re.search(r'<script\b', html)

def test_use_strict(html):
    assert "'use strict'" in html or '"use strict"' in html

def test_storage_key_defined(html):
    assert "STORAGE_KEY" in html
    assert "weather_last_city" in html

def test_wmo_codes_defined(html):
    assert "WMO_CODES" in html

def test_wmo_clear_sky_entry(html):
    assert "Clear Sky" in html

def test_wmo_thunderstorm_entry(html):
    assert "Thunderstorm" in html

def test_geocoding_api_url(html):
    assert "geocoding-api.open-meteo.com" in html

def test_weather_api_url(html):
    assert "api.open-meteo.com/v1/forecast" in html

def test_temperature_conversion_formula(html):
    # °C to °F: * 9 / 5 + 32
    assert re.search(r'\*\s*9\s*/\s*5\s*\+\s*32', html)

def test_wind_conversion_factor(html):
    # km/h to mph factor 0.621371
    assert "0.621371" in html

def test_localstorage_set(html):
    assert "localStorage.setItem" in html

def test_localstorage_get(html):
    assert "localStorage.getItem" in html

def test_enter_key_listener(html):
    assert re.search(r"e\.key\s*===\s*['\"]Enter['\"]", html)

def test_search_function_defined(html):
    assert re.search(r'(async\s+)?function\s+search\s*\(', html)

def test_geocode_function_defined(html):
    assert re.search(r'(async\s+)?function\s+geocode\s*\(', html)

def test_fetch_weather_function_defined(html):
    assert re.search(r'(async\s+)?function\s+fetchWeather\s*\(', html)

def test_display_weather_function_defined(html):
    assert re.search(r'function\s+displayWeather\s*\(', html)

def test_render_units_function_defined(html):
    assert re.search(r'function\s+renderUnits\s*\(', html)

def test_set_loading_function_defined(html):
    assert re.search(r'function\s+setLoading\s*\(', html)

def test_show_error_function_defined(html):
    assert re.search(r'function\s+showError\s*\(', html)

def test_empty_city_error_message(html):
    assert "Please enter a city name." in html

def test_state_object_defined(html):
    assert re.search(r'const\s+state\s*=\s*\{', html)

def test_state_has_unit_field(html):
    assert re.search(r"unit\s*:\s*['\"]C['\"]", html)

def test_unit_toggle_click_handler(html):
    assert re.search(r"unitToggle.*addEventListener|addEventListener.*unitToggle", html, re.DOTALL)