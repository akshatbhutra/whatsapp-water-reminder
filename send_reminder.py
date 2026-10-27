import os
import sys
import requests

# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

EVOLUTION_API_URL = os.getenv("EVOLUTION_API_URL")
EVOLUTION_API_KEY = os.getenv("EVOLUTION_API_KEY")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

# ============================================================
# VALIDATE CONFIGURATION
# ============================================================

def validate_config():
    missing = []
    if not EVOLUTION_API_URL:
        missing.append("EVOLUTION_API_URL")
    if not EVOLUTION_API_KEY:
        missing.append("EVOLUTION_API_KEY")
    if not WHATSAPP_NUMBER:
        missing.append("WHATSAPP_NUMBER")

    if missing:
        print("❌ Error: Missing environment variables: " + ", ".join(missing))
        sys.exit(1)

# ============================================================
# SEND WHATSAPP MESSAGE
# ============================================================

def send_water_reminder():
    validate_config()
    
    # Clean base URL and ensure it points to the sendText endpoint like your reference script
    base_url = EVOLUTION_API_URL.rstrip("/")
    
    # If the user put just the base server URL, automatically append the message path & instance placeholder or use as-is if full path provided
    if not "/message/sendText/" in base_url:
        print("❌ Error: EVOLUTION_API_URL must include the full path: e.g., https://your-api.com/message/sendText/YOUR_INSTANCE_NAME")
        sys.exit(1)

    headers = {
        "apikey": EVOLUTION_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "number": WHATSAPP_NUMBER,
        "text": "💧 Friendly reminder: Time to drink a glass of water and stay hydrated!"
    }

    print(f"Sending water reminder to WhatsApp via: {base_url}")
    response = requests.post(base_url, json=payload, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    response.raise_for_status()
    print("✅ Water reminder sent successfully!")

if __name__ == "__main__":
    send_water_reminder()