import os
import time
import json
import youtube_dl

import discord
from discord.ext import commands

class spam(commands.Cog):

    players = {}

    def __init__(self, client):
        self.client = client
        self.config = json.load(open("config.json"))

    @commands.Cog.listener()
    async def on_ready(self):
        print("spam loaded.")

    @commands.command(name = "joinChannel")
    async def voice_join(self, ctx, channel_index):

        channel = ctx.guild.voice_channels[int(channel_index)]
        await channel.connect()

    @commands.command(name = "localChannel")
    async def voice_join_2(self, ctx):

        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command(name = "Send")
    async def picture(self, ctx, loops):
        for i in range(int(loops)):
            await ctx.send(file=discord.File('ok.png'))

    @commands.command(name = "Play")
    async def play(self,ctx,channel_index):
        """
        guild = ctx.message.guild
        voice_client = guild.voice_client

        player = await voice_client.create_ytdl_player(url)

        players[guild.id] = player
        player.start()
        """

        voice_channel = ctx.message.author.voice.channel

        channel = ctx.guild.voice_channels[int(channel_index)]

        vc = ctx.guild.voice_client

        url = 'https://www.youtube.com/watch?v=MbhXIddT2YY'
        player = await vc.create_ytdl_player(url)
        players[guild.id] = player
        player.start()


def setup(client):
    client.add_cog(spam(client))
