# Weather CLI

A fast, simple command-line weather tool that fetches current weather conditions for any location.

## Features

- 🌡️ Current temperature (Celsius and Fahrenheit)
- 💨 Wind speed and direction
- 💧 Humidity levels
- 👁️ Visibility
- ☀️ UV index
- 🌍 Works for any location worldwide
- 🔓 No API key required

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli

# Make the script executable (Unix/Linux/Mac)
chmod +x weather.py
```

## Usage

```bash
# Get weather for your current location (based on IP)
python3 weather.py

# Get weather for a specific city
python3 weather.py London

# Get weather for a city with spaces in name
python3 weather.py New York

# Get weather for a specific location
python3 weather.py "Paris, France"
```

## Requirements

- Python 3.6 or higher
- Internet connection
- No external dependencies (uses only Python standard library)

## Examples

```bash
$ python3 weather.py Tokyo

Fetching weather data...

🌍 Weather for Tokyo, Japan
==================================================
Temperature: 18°C / 64°F
Feels Like: 16°C / 61°F
Condition: Partly cloudy
Humidity: 65%
Wind: 15 km/h NE
Pressure: 1015 mb
Visibility: 10 km
UV Index: 5
```

## API

This tool uses the [wttr.in](https://wttr.in) service, which provides weather data from multiple sources.

## License

MIT License - feel free to use this in your own projects!
