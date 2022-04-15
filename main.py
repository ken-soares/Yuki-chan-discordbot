import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

read_mode = input("1. Enter bot token\n2.Read token from .env file(1/2):")
if int(read_mode) == 1:
    token = input("Please enter bot token: ")
else:
    token = str(os.getenv("TOKEN"))

default_intents = discord.Intents.default()
default_intents.members = True
client = commands.Bot( command_prefix = "y!",intents=default_intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("y!help → list commands"))
    print("Yuki-chan has been started")

@client.event
async def on_member_join(member):
    await member.send("Welcome to this server :partying_face: I am Yuki-chan, feel free to enter `y!help` to see my commands!")
   
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
