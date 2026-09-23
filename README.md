# Multi-API Real-Time Dashboard

A Python CLI dashboard that fetches real-time data from two live REST APIs — Weather and Currency — with production-style error handling.

## Features

- Fetches live weather data from wttr.in API
- Fetches live exchange rates from open.er-api.com
- Handles timeouts, connection errors, and rate limits
- Shows 6 currency rates (INR, EUR, GBP, AED, SGD, JPY)
- Displays weather tip based on temperature
- Allows searching another city

## Tech Stack

- Python 3.x
- requests (HTTP calls)
- JSON (data parsing)
- datetime (timestamps)

## APIs Used

| API | URL | Purpose |
|-----|-----|---------|
| Weather | wttr.in | Live weather data |
| Currency | open.er-api.com | Live exchange rates |

## Error Handling

- `requests.exceptions.Timeout` — server too slow
- `requests.exceptions.ConnectionError` — no internet
- Status 429 — rate limited
- Status 404 — city not found
- Timeout set to 8 seconds on every call

## Installation

git clone https://github.com/mukesh-mlops/multi-api-dashboard.git
cd multi-api-dashboard
pip install requests
python multi_api_dashboard.py

## Built By

S. Mukesh Kumar
GitHub: https://github.com/mukesh-mlops
