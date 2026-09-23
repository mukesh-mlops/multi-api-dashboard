import requests
from datetime import datetime

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        r = requests.get(url, timeout=8)
        
        print(f"  [Weather]  Status Code: {r.status_code}")
        
        if r.status_code == 200:
            c = r.json()["current_condition"][0]
            return {
                "city": city,
                "temp": c["temp_C"],
                "feels": c["FeelsLikeC"],
                "humidity": c["humidity"],
                "condition": c["weatherDesc"][0]["value"],
                "wind": c["windspeedKmph"],
            }
        return None
    except requests.exceptions.Timeout:
        print("  [Weather]  Timeout — server slow")
        return None
    except requests.exceptions.ConnectionError:
        print("  [Weather]  No internet connection")
        return None
    except Exception as e:
        print(f"  [Weather]  Error: {e}")
        return None

def get_exchange_rates(base="USD"):
    try:
        url = f"https://open.er-api.com/v6/latest/{base}"
        r = requests.get(url, timeout=8)
        
        print(f"  [Currency] Status Code: {r.status_code}")
        
        if r.status_code == 200:
            rates = r.json()["rates"]
            needed = ["INR", "EUR", "GBP", "AED", "SGD", "JPY"]
            return {k: round(rates[k], 4) for k in needed if k in rates}
        elif r.status_code == 429:
            print("  [Currency] Rate limited")
            return None
        return None
    except requests.exceptions.Timeout:
        print("  [Currency] Timeout")
        return None
    except requests.exceptions.ConnectionError:
        print("  [Currency] No internet")
        return None
    except Exception as e:
        print(f"  [Currency] Error: {e}")
        return None

def display_dashboard(city="Chennai"):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("\n" + "="*55)
    print("   MULTI-API REAL-TIME DASHBOARD")
    print(f"   Updated: {now}")
    print("   Built by: S. Mukesh Kumar")
    print("="*55)
    print("\n  Fetching from 2 live APIs...")

    weather = get_weather(city)
    rates = get_exchange_rates("USD")

    fetched = sum([weather is not None, rates is not None])
    print(f"  Fetched {fetched}/2 APIs successfully\n")

    print(f"  WEATHER — {city.upper()}")
    print("  " + "-"*45)
    if weather:
        print(f"  Temperature : {weather['temp']}°C (feels {weather['feels']}°C)")
        print(f"  Condition   : {weather['condition']}")
        print(f"  Humidity    : {weather['humidity']}%")
        print(f"  Wind        : {weather['wind']} km/h")
        temp = int(weather["temp"])
        tip = "Very hot — carry water!" if temp > 35 else "Cool — carry jacket!" if temp < 20 else "Pleasant weather!"
        print(f"  Tip         : {tip}")
    else:
        print("  Weather data unavailable")

    print(f"\n  CURRENCY — 1 USD =")
    print("  " + "-"*45)
    if rates:
        for currency, rate in sorted(rates.items()):
            print(f"  {currency}  :  {rate}")
    else:
        print("  Currency data unavailable")

    print("\n" + "="*55)
    print(f"  Dashboard complete — {fetched}/2 APIs fetched")
    print("="*55)

def main():
    display_dashboard("Chennai")
    another = input("\n  Enter another city (or press Enter to skip): ").strip()
    if another:
        display_dashboard(another)

main()