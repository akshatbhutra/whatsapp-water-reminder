# WhatsApp Water Reminder Bot (GitHub Actions)

This repository sets up an automated hourly water reminder sent via Evolution API to WhatsApp using GitHub Actions.

## Setup Instructions

1. Push these files to your GitHub repository.
2. Go to **Settings > Secrets and variables > Actions** in your repository.
3. Add the following repository secrets:
   - `EVOLUTION_API_URL`: Full endpoint URL (e.g., `https://api.yourdomain.com/message/sendText/your_instance_name`)
   - `EVOLUTION_API_KEY`: Your Evolution API Key
   - `WHATSAPP_NUMBER`: Recipient phone number with country code (e.g., `919876543210`)
