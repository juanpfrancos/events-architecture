import requests
import json
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()
AUTH_HEADER = {
    "Authorization": f"Bearer {os.getenv('WPP_TOKEN')}",
    "Content-Type": "application/json"
}

URL = f"https://graph.facebook.com/v20.0/{os.getenv('BUSINESS_ID')}/messages"

"""
Function to send a message to a whatsapp number
"""
def send_message(phone, message_text):
    message = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "template",
        "template": {
            "name": "event_message",
            "language": {
                "code": "es_ES"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": f"{message_text}"
                        }
                    ]
                }
            ]
        }
    }
    response = requests.post(URL, headers=AUTH_HEADER, data=json.dumps(message))
    if response.status_code == 200:
        return f"Message sent successfully to {phone}"
    else:
        raise HTTPException(status_code=500, detail=f"Error sending the message to {phone}: {response.text}")