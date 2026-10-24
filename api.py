
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=31.52&longitude=74.36&current_weather=true"

response = requests.get(url, timeout=15)

print("Status Code:", response.status_code)

response.raise_for_status()
data = response.json()

print("Windspeed:", data["current_weather"]["windspeed"])
print("Temperature:", data["current_weather"]["temperature"])
