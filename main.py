import asyncio
import os

import discord
from discord import app_commands
from discord.ext import commands, tasks

from utils.config import token

intents = discord.Intents.all()
intents.message_content = True
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Sync'd all application commands @%H:%M:%S\n"
              f"%m/%d/%Y\n"
              f"-----")
        print(f'Logged in as {client.user}')
        print('-----')
        await tree.sync()

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


client.run(token,
           reconnect=True)
