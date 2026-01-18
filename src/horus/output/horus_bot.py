import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Intents control what events your bot receives.
intents = discord.Intents.default()
intents.message_content = True  # required for prefix commands that read message text

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id={bot.user.id})")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("pong 🏓")

@bot.command()
async def say(ctx: commands.Context, *, msg: str):
    # repeats whatever you type after !say
    await ctx.send(msg)

bot.run(TOKEN)