# Requirements — Simple Weather App

## What to build
A single-page web application that lets a user check current weather conditions for any city.

## Features
- Search for a city via a text input and a button
- Display current temperature, weather condition, humidity, and wind speed
- Show a weather icon or emoji that reflects current conditions (sunny, cloudy, rainy, etc.)
- Toggle between Celsius and Fahrenheit units
- Remember the last searched city so it reloads on page refresh

## Tech
- Plain HTML, CSS, JavaScript — no framework required
- Single file output preferred (index.html)
- Uses the Open-Meteo API (free, no API key needed) for weather data
- Uses the Open-Meteo Geocoding API to resolve city names to coordinates
- Must work in Chrome without any build step

## Acceptance criteria
- All 5 features work correctly
- City search resolves names to coordinates and fetches live weather data
- Unit toggle switches between C and F without re-fetching
- Last searched city is restored from localStorage on load
- No console errors on load or interaction
- Page is usable on a mobile screen (375px wide)
- Display a 5-day forecast section showing daily high and low temperatures
