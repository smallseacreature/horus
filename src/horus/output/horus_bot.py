from dotenv import load_dotenv
import os
import requests

#TODO build discord messages by target
load_dotenv()

WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK:
    raise RuntimeError("DISCORD_WEBHOOK_URL not loaded")

def discord_notify(msg):
    payload = {
        "content": msg,
    }

    requests.post(str(WEBHOOK), json=payload, timeout=15)