from dotenv import load_dotenv
import os
import requests

#TODO build discord messages by target
load_dotenv()

WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK:
    raise RuntimeError("DISCORD_WEBHOOK_URL not loaded")

def no_embed(url) -> str:
    """wrap urls in <> so discord bot doesn't embed them"""
    return f"<{url}>"

def discord_notify(msg: str):
    requests.post(str(WEBHOOK), json={"content": msg}, timeout=15)