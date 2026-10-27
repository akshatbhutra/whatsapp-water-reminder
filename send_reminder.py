import os
import requests

url = os.getenv("EVOLUTION_API_URL")
api_key = os.getenv("EVOLUTION_API_KEY")
phone = os.getenv("WHATSAPP_NUMBER")

headers = {
    "apikey": api_key,
    "Content-Type": "application/json"
}

payload = {
    "number": phone,
    "text": "💧 Friendly reminder: Time to drink a glass of water and stay hydrated!"
}

response = requests.post(url, json=payload, headers=headers)
print(f"Status: {response.status_code}")
print(response.text)
response.raise_for_status()
