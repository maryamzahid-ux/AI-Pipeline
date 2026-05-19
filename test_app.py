import re
import pathlib
import pytest

HTML_FILE = pathlib.Path(__file__).parent / "index.html"


@pytest.fixture(scope="module")
def html():
    return HTML_FILE.read_text(encoding="utf-8")


# ── File & Document ───────────────────────────────────────────────────────────

class TestDocument:
    def test_file_exists(self):
        assert HTML_FILE.exists(), "index.html not found"

    def test_doctype(self, html):
        assert html.strip().startswith("<!DOCTYPE html>")

    def test_lang_en(self, html):
        assert re.search(r'<html[^>]+lang=["\']en["\']', html)

    def test_charset_utf8(self, html):
        assert re.search(r'<meta[^>]+charset=["\']UTF-8["\']', html, re.IGNORECASE)

    def test_viewport_meta(self, html):
        assert re.search(r'<meta[^>]+name=["\']viewport["\']', html)

    def test_title(self, html):
        assert re.search(r'<title>\s*Weather App\s*</title>', html)


# ── Header ────────────────────────────────────────────────────────────────────

class TestHeader:
    def test_h1_text(self, html):
        assert re.search(r'<h1[^>]*>\s*Weather\s*</h1>', html)

    def test_subtitle(self, html):
        assert "Live conditions for any city" in html


# ── Search Bar ────────────────────────────────────────────────────────────────

class TestSearchBar:
    def test_search_bar_div(self, html):
        assert re.search(r'class=["\'][^"\']*search-bar[^"\']*["\']', html)

    def test_city_input_exists(self, html):
        assert re.search(r'id=["\']cityInput["\']', html)

    def test_city_input_type_text(self, html):
        assert re.search(r'<input[^>]+id=["\']cityInput["\']', html)
        assert re.search(r'<input[^>]+type=["\']text["\']', html)

    def test_city_input_placeholder(self, html):
        assert re.search(r'placeholder=["\']Enter city name', html)

    def test_autocomplete_off(self, html):
        assert re.search(r'autocomplete=["\']off["\']', html)

    def test_search_button_exists(self, html):
        assert re.search(r'id=["\']searchBtn["\']', html)

    def test_search_button_text(self, html):
        assert re.search(r'id=["\']searchBtn["\'][^>]*>\s*Search\s*<', html)


# ── Feedback & Loading Elements ───────────────────────────────────────────────

class TestFeedbackElements:
    def test_error_msg_exists(self, html):
        assert re.search(r'id=["\']errorMsg["\']', html)

    def test_error_msg_class(self, html):
        assert re.search(r'class=["\'][^"\']*error-msg[^"\']*["\']', html)

    def test_spinner_exists(self, html):
        assert re.search(r'id=["\']spinner["\']', html)

    def test_spinner_class(self, html):
        assert re.search(r'class=["\'][^"\']*spinner[^"\']*["\']', html)


# ── Weather Card ──────────────────────────────────────────────────────────────

class TestWeatherCard:
    def test_card_exists(self, html):
        assert re.search(r'id=["\']card["\']', html)

    def test_city_name(self, html):
        assert re.search(r'id=["\']cityName["\']', html)

    def test_country_name(self, html):
        assert re.search(r'id=["\']countryName["\']', html)

    def test_weather_icon(self, html):
        assert re.search(r'id=["\']weatherIcon["\']', html)

    def test_condition(self, html):
        assert re.search(r'id=["\']condition["\']', html)

    def test_temperature(self, html):
        assert re.search(r'id=["\']temperature["\']', html)

    def test_unit_toggle(self, html):
        assert re.search(r'id=["\']unitToggle["\']', html)

    def test_unit_toggle_aria_label(self, html):
        assert re.search(r'aria-label=["\']Toggle temperature unit["\']', html)

    def test_celsius_btn(self, html):
        assert re.search(r'id=["\']celsiusBtn["\']', html)

    def test_fahrenheit_btn(self, html):
        assert re.search(r'id=["\']fahrenheitBtn["\']', html)

    def test_celsius_active_by_default(self, html):
        assert re.search(r'id=["\']celsiusBtn["\'][^>]*class=["\'][^"\']*active', html)

    def test_humidity_element(self, html):
        assert re.search(r'id=["\']humidity["\']', html)

    def test_wind_speed_element(self, html):
        assert re.search(r'id=["\']windSpeed["\']', html)

    def test_humidity_label(self, html):
        assert "Humidity" in html

    def test_wind_speed_label(self, html):
        assert "Wind Speed" in html


# ── CSS Visibility Classes ────────────────────────────────────────────────────

class TestCSSVisibility:
    def test_error_msg_default_hidden(self, html):
        assert re.search(r'\.error-msg\s*\{[^}]*display\s*:\s*none', html, re.DOTALL)

    def test_error_msg_visible_shown(self, html):
        assert re.search(r'\.error-msg\.visible\s*\{[^}]*display\s*:\s*block', html, re.DOTALL)

    def test_spinner_default_hidden(self, html):
        assert re.search(r'\.spinner\s*\{[^}]*display\s*:\s*none', html, re.DOTALL)

    def test_spinner_visible_shown(self, html):
        assert re.search(r'\.spinner\.visible\s*\{[^}]*display\s*:\s*block', html, re.DOTALL)

    def test_card_default_hidden(self, html):
        assert re.search(r'\.card\s*\{[^}]*display\s*:\s*none', html, re.DOTALL)

    def test_card_visible_shown(self, html):
        assert re.search(r'\.card\.visible\s*\{[^}]*display\s*:\s*block', html, re.DOTALL)


# ── CSS Design Tokens & Layout ────────────────────────────────────────────────

class TestCSSDesign:
    def test_css_var_bg(self, html):
        assert re.search(r'--bg\s*:', html)

    def test_css_var_surface(self, html):
        assert re.search(r'--surface\s*:', html)

    def test_css_var_accent(self, html):
        assert re.search(r'--accent\s*:', html)

    def test_css_var_text(self, html):
        assert re.search(r'--text\s*:', html)

    def test_css_var_muted(self, html):
        assert re.search(r'--muted\s*:', html)

    def test_box_sizing_border_box(self, html):
        assert re.search(r'box-sizing\s*:\s*border-box', html)

    def test_body_flex(self, html):
        assert re.search(r'body\s*\{[^}]*display\s*:\s*flex', html, re.DOTALL)

    def test_details_grid(self, html):
        assert re.search(r'\.details\s*\{[^}]*display\s*:\s*grid', html, re.DOTALL)

    def test_spin_keyframes(self, html):
        assert re.search(r'@keyframes\s+spin', html)

    def test_mobile_media_query(self, html):
        assert re.search(r'@media\s*\(\s*max-width\s*:\s*400px\s*\)', html)

    def test_search_bar_max_width(self, html):
        assert re.search(r'\.search-bar\s*\{[^}]*max-width\s*:\s*480px', html, re.DOTALL)


# ── JavaScript: State & Constants ─────────────────────────────────────────────

class TestJSState:
    def test_use_strict(self, html):
        assert "'use strict'" in html

    def test_storage_key(self, html):
        assert re.search(r"STORAGE_KEY\s*=\s*['\"]weather_last_city['\"]", html)

    def test_state_object(self, html):
        assert re.search(r'\bstate\s*=\s*\{', html)

    def test_state_temp_c_null(self, html):
        assert re.search(r'tempC\s*:\s*null', html)

    def test_state_wind_kmh_null(self, html):
        assert re.search(r'windKmh\s*:\s*null', html)

    def test_state_unit_celsius(self, html):
        assert re.search(r"unit\s*:\s*['\"]C['\"]", html)


# ── JavaScript: Functions ─────────────────────────────────────────────────────

class TestJSFunctions:
    def test_set_loading(self, html):
        assert re.search(r'function\s+setLoading\s*\(', html)

    def test_show_error(self, html):
        assert re.search(r'function\s+showError\s*\(', html)

    def test_clear_error(self, html):
        assert re.search(r'function\s+clearError\s*\(', html)

    def test_render_units(self, html):
        assert re.search(r'function\s+renderUnits\s*\(', html)

    def test_geocode(self, html):
        assert re.search(r'async\s+function\s+geocode\s*\(', html)

    def test_fetch_weather(self, html):
        assert re.search(r'async\s+function\s+fetchWeather\s*\(', html)

    def test_display_weather(self, html):
        assert re.search(r'function\s+displayWeather\s*\(', html)

    def test_search(self, html):
        assert re.search(r'async\s+function\s+search\s*\(', html)


# ── JavaScript: Event Listeners ───────────────────────────────────────────────

class TestJSEvents:
    def test_search_btn_click(self, html):
        assert re.search(r"searchBtn.*?addEventListener\s*\(\s*['\"]click['\"]", html, re.DOTALL)

    def test_city_input_keydown(self, html):
        assert re.search(r"cityInput.*?addEventListener\s*\(\s*['\"]keydown['\"]", html, re.DOTALL)

    def test_enter_key_triggers_search(self, html):
        assert re.search(r"e\.key\s*===\s*['\"]Enter['\"]", html)

    def test_unit_toggle_click(self, html):
        assert re.search(r"unitToggle.*?addEventListener\s*\(\s*['\"]click['\"]", html, re.DOTALL)

    def test_unit_toggle_flips_state(self, html):
        assert re.search(r"state\.unit\s*===\s*['\"]C['\"]", html)


# ── JavaScript: API Calls ─────────────────────────────────────────────────────

class TestJSAPI:
    def test_geocoding_api_url(self, html):
        assert "geocoding-api.open-meteo.com" in html

    def test_weather_api_url(self, html):
        assert "api.open-meteo.com/v1/forecast" in html

    def test_encode_uri_component(self, html):
        assert re.search(r'encodeURIComponent\s*\(', html)

    def test_temperature_2m_param(self, html):
        assert "temperature_2m" in html

    def test_humidity_param(self, html):
        assert "relative_humidity_2m" in html

    def test_wind_speed_param(self, html):
        assert "wind_speed_10m" in html

    def test_weather_code_param(self, html):
        assert "weather_code" in html

    def test_wind_speed_unit_kmh(self, html):
        assert re.search(r"wind_speed_unit.*kmh|kmh.*wind_speed_unit", html)

    def test_timezone_auto(self, html):
        assert re.search(r"timezone.*auto|auto.*timezone", html)


# ── JavaScript: Data Processing ───────────────────────────────────────────────

class TestJSProcessing:
    def test_celsius_to_fahrenheit_formula(self, html):
        assert re.search(r'tempC\s*\*\s*9\s*/\s*5\s*\+\s*32', html)

    def test_kmh_to_mph_factor(self, html):
        assert "0.621371" in html

    def test_math_round(self, html):
        assert re.search(r'Math\.round\s*\(', html)

    def test_trim_input(self, html):
        assert re.search(r'\.trim\s*\(\s*\)', html)

    def test_filter_boolean_country(self, html):
        assert re.search(r'\.filter\s*\(\s*Boolean\s*\)', html)

    def test_local_storage_set(self, html):
        assert re.search(r'localStorage\.setItem\s*\(\s*STORAGE_KEY', html)

    def test_local_storage_get(self, html):
        assert re.search(r'localStorage\.getItem\s*\(\s*STORAGE_KEY', html)

    def test_local_storage_try_catch(self, html):
        # Both localStorage accesses must be guarded
        catches = len(re.findall(r'\}\s*catch\s*\(', html))
        assert catches >= 2, "localStorage calls should each be in try/catch"


# ── JavaScript: Error Messages ────────────────────────────────────────────────

class TestJSErrors:
    def test_empty_city_message(self, html):
        assert "Please enter a city name" in html

    def test_city_not_found_message(self, html):
        assert "not found" in html

    def test_geocoding_failure_message(self, html):
        assert "Geocoding request failed" in html

    def test_weather_failure_message(self, html):
        assert "Weather request failed" in html

    def test_generic_error_fallback(self, html):
        assert "Something went wrong" in html


# ── WMO Code Table ────────────────────────────────────────────────────────────

class TestWMOCodes:
    CODES = [0, 1, 2, 3, 45, 48, 51, 53, 55, 56, 57,
             61, 63, 65, 66, 67, 71, 73, 75, 77,
             80, 81, 82, 85, 86, 95, 96, 99]

    LABELS = [
        "Clear Sky", "Mainly Clear", "Partly Cloudy", "Overcast",
        "Foggy", "Icy Fog", "Light Drizzle", "Drizzle", "Heavy Drizzle",
        "Light Rain", "Rain", "Heavy Rain",
        "Light Snow", "Snow", "Heavy Snow",
        "Light Showers", "Showers", "Heavy Showers",
        "Thunderstorm",
    ]

    def test_wmo_codes_object_exists(self, html):
        assert re.search(r'WMO_CODES\s*=\s*\{', html)

    @pytest.mark.parametrize("code", CODES)
    def test_wmo_code_present(self, html, code):
        assert re.search(rf'\b{code}\s*:', html), f"WMO code {code} missing"

    @pytest.mark.parametrize("label", LABELS)
    def test_wmo_label_present(self, html, label):
        assert label in html, f"WMO label '{label}' missing"

    def test_wmo_emoji_fields(self, html):
        emojis = re.findall(r"emoji\s*:", html)
        assert len(emojis) >= len(self.CODES)

    def test_wmo_fallback_unknown(self, html):
        assert "Unknown" in html

    def test_wmo_clear_sky_code_0(self, html):
        assert re.search(r'0\s*:\s*\{[^}]*Clear Sky', html, re.DOTALL)

    def test_wmo_thunderstorm_code_95(self, html):
        assert re.search(r'95\s*:\s*\{[^}]*Thunderstorm', html, re.DOTALL)


# ── Temperature Conversion (pure Python verification) ─────────────────────────

class TestTemperatureConversionLogic:
    """Verify the math used in the JS is correct."""

    @staticmethod
    def to_f(c):
        return round(c * 9 / 5 + 32)

    @staticmethod
    def to_mph(kmh):
        return round(kmh * 0.621371)

    def test_freezing(self):
        assert self.to_f(0) == 32

    def test_boiling(self):
        assert self.to_f(100) == 212

    def test_body_temp(self):
        assert self.to_f(37) == 99

    def test_crossover_point(self):
        assert self.to_f(-40) == -40

    def test_mph_zero(self):
        assert self.to_mph(0) == 0

    def test_mph_100_kmh(self):
        assert self.to_mph(100) == 62

    def test_mph_160_kmh(self):
        assert self.to_mph(160) == 99