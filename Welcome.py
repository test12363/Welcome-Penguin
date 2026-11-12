# Welcome Bot - Created by 6YuaZ (Penguin)
# Thanks for supporting the project! Everything here is clean and modular.

import os
import json
import asyncio
import discord
from discord.ext import commands

# Let's load your settings from the config file
with open("welcome_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Quick tip: If you host this online (like Render/Railway), set an env variable called "TOKEN"
# Otherwise, it will just grab the token straight from your welcome_config.json file
TOKEN = os.getenv("TOKEN", config["token"])

# Make sure you turn ON "Server Members Intent" and "Message Content Intent" in the Discord Dev Portal!
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} | Penguin Welcome is online and ready!")

async def main():
    async with bot:
        # Loading our welcome module from the cogs folder
        await bot.load_extension("cogs.welcome_cog")
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
