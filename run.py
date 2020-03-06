import os
import json

import discord
from discord.ext import commands

config = json.load(open("config.json"))
print("Setting up...")

bot = commands.Bot(
    command_prefix = config["prefix"]
)

# loading commands
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(config["token"])
