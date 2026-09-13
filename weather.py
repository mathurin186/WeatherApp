"""
Simple CLI weather tool.
Uses Open-Meteo (free, no API key required):
  - Geocoding: https://open-meteo.com/en/docs/geocoding-api
  - Weather:   https://open-meteo.com/en/docs
"""

import sys

import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# Open-Meteo returns numeric weather codes; this maps them to plain text.
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def get_coordinates(city_name, country_code="US"):
    """
    Look up latitude/longitude for a city name.
    Returns None if not found. If multiple matches are found, prompts
    the user to pick one.

    country_code: ISO 3166-1 alpha-2 code (e.g. "US") to restrict results to
    one country. Pass None to search worldwide.
    """
    params = {"name": city_name, "count": 10}
    if country_code:
        params["countryCode"] = country_code

    response = requests.get(GEOCODE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    results = data.get("results")
    if not results:
        return None

    if len(results) == 1:
        place = results[0]
    else:
        place = choose_from_matches(results)

    return {
        "name": place["name"],
        "region": place.get("admin1", ""),
        "country": place.get("country", ""),
        "latitude": place["latitude"],
        "longitude": place["longitude"],
    }


def choose_from_matches(results):
    """Print multiple location matches and let the user pick one."""
    print("\nMultiple matches found:")
    for index, place in enumerate(results, start=1):
        region = place.get("admin1", "")
        country = place.get("country", "")
        location_bits = ", ".join(part for part in [region, country] if part)
        print(f"  {index}. {place['name']} ({location_bits})")

    while True:
        choice = input(f"Choose a location (1-{len(results)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(results):
            return results[int(choice) - 1]
        print("Invalid choice, try again.")


def get_weather(latitude, longitude):
    """Fetch current weather for a given latitude/longitude."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
    }
    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()["current"]


def describe_weather_code(code):
    return WEATHER_CODES.get(code, f"Unknown conditions (code {code})")


def main():
    if len(sys.argv) > 1:
        city_name = " ".join(sys.argv[1:]).strip()
    else:
        city_name = input("Enter a city name: ").strip()
    if not city_name:
        print("Please enter a city name.")
        return

    try:
        location = get_coordinates(city_name)
    except requests.RequestException as error:
        print(f"Network error while looking up city: {error}")
        return

    if location is None:
        print(f"Could not find a location matching '{city_name}'.")
        return

    try:
        current = get_weather(location["latitude"], location["longitude"])
    except requests.RequestException as error:
        print(f"Network error while fetching weather: {error}")
        return

    location_label = ", ".join(
        part for part in [location["name"], location["region"], location["country"]] if part
    )
    print(f"\nWeather for {location_label}")
    print(f"  Conditions:  {describe_weather_code(current['weather_code'])}")
    print(f"  Temperature: {current['temperature_2m']}°F")
    print(f"  Humidity:    {current['relative_humidity_2m']}%")
    print(f"  Wind speed:  {current['wind_speed_10m']} mph\n")


if __name__ == "__main__":
    main()
