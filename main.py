import discord
import os
from discord.ext import commands


token = input("Please enter bot token: ")

default_intents = discord.Intents.default()
default_intents.members = True
client = commands.Bot( command_prefix = "y!",intents=default_intents)

@client.event
async def on_ready():
    print("Yuki-chan has been started")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
