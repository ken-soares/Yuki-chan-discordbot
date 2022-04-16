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
client = commands.Bot( command_prefix = "y!",intents=default_intents, help_command=None)

@client.command()
async def help(ctx):
    embed = discord.Embed(
            title="Help",
            description="Yuki-chan's commands",
            color=discord.Color.blue()
            )
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/338Ir-6ZyikfVjTqJbDdhe2bbssmTercviUrow8DVOM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/926836893121912852/69a147f933d4223dbf14945199be2ae6.webp?width=690&height=690')
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name='Relationships',value="`kiss`, `hug`, `pat`, `slap`, `cry`")
    embed.add_field(name='Fun',value="`meme`, `emojify`, `randomify`, `hack`, `dog`, `cat`",inline=False)
    embed.add_field(name='Minigames',value="`guess`, `destiny`, `imposter`, `rockpaperscissors`",inline=False)
    embed.add_field(name='Moderation',value="`ban`, `unban`, `kick`, `clear`",inline=False)
    embed.add_field(name='Misc',value="`coinflip`, `getpfp`, `docs`, `changelog`",inline=False)
    await ctx.send(embed=embed)

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
