import os
import random
import json

import discord
from discord.ext import commands

class default(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open("config.json"))
        self.greetings = json.load(open("greetings.json"))

    @commands.Cog.listener()
    async def on_ready(self):
        print("default loaded.")
        await self.client.change_presence(status=discord.Status.online,
            activity=discord.Activity(type=discord.ActivityType.watching,name="Muharis"))

    # simple greet command
    @commands.command(aliases = ["Hello", "Hi", "Yo", "Howdy"])
    async def greet(self, ctx):
        await ctx.send(random.choice(self.greetings))

    @commands.command(aliases = ["Die","begone","Begone","thot"])
    async def die(self, ctx):
        await ctx.send("NOOooooo...")
        await ctx.bot.logout()

def setup(client):
    client.add_cog(default(client))
