#!/usr/bin/env python3
"""
Simple CLI tool to fetch current weather using wttr.in API
No API key required - completely free
"""

import sys
import urllib.request
import json

def get_weather(location=""):
    """Fetch weather data for a location"""
    if not location:
        # Get weather for current location based on IP
        url = "https://wttr.in/?format=j1"
    else:
        # Get weather for specified location
        url = f"https://wttr.in/{location}?format=j1"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching weather: {e}")
        sys.exit(1)

def display_weather(data):
    """Display weather in a clean format"""
    current = data['current_condition'][0]
    area = data['nearest_area'][0]

    print(f"\n🌍 Weather for {area['areaName'][0]['value']}, {area['country'][0]['value']}")
    print(f"{'=' * 50}")
    print(f"Temperature: {current['temp_C']}°C / {current['temp_F']}°F")
    print(f"Feels Like: {current['FeelsLikeC']}°C / {current['FeelsLikeF']}°F")
    print(f"Condition: {current['weatherDesc'][0]['value']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['windspeedKmph']} km/h {current['winddir16Point']}")
    print(f"Pressure: {current['pressure']} mb")
    print(f"Visibility: {current['visibility']} km")
    print(f"UV Index: {current['uvIndex']}")
    print()

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        location = " ".join(sys.argv[1:])
    else:
        location = ""

    print("Fetching weather data...")
    data = get_weather(location)
    display_weather(data)

if __name__ == "__main__":
    main()
