from dotenv import load_dotenv
from pathlib import Path
import os
import requests

load_dotenv()

WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
if not WEBHOOK:
    raise RuntimeError("DISCORD_WEBHOOK_URL not loaded")

def discord_notify(msg: str):
    requests.post(WEBHOOK, json={"content": msg}, timeout=15)

discord_notify("test alert")
