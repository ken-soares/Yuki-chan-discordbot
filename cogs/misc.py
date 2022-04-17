import discord
import random
from random import choice
import asyncio
import aiohttp
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    emails = ["michel", "robert", "gitgud", "baguette", "potatoe", "xxGAmErxX", "bob", "rob", "uwu", "owo", "gaeming", "ytb",
            "richard", "prohakkker","iuselinuxbtw"]

    passwords = ["ihaveacrushonavtuber", "potatoesarecool", "gamingisFun238948394", "helloWorld!", 
            "bigfatpooplololol", "sophisticatedCucumber69420", "neverGonnaGiveYouUp", "ihavedepression"]
    quotes = ["I love illegal stuff you know?", "I would totally cheat on my gf",
            "I forgot to tell you that I'm 100% racist", "I do have an IQ of 420.",
            "Is 5 inches really that bad?", "JPop > Kpop change my mind."]
    randomWord = ['uwu', "owo", "cringe", "based", "gay", "f*ck", "kms", "kys", "food", "simp"]

    @commands.command()
    async def hack(self,ctx,*,member:discord.Member):
        message = await ctx.send(f"Hacking {member.mention}")
        await asyncio.sleep(1)
        await message.edit(content=f"`Finding discord login (2fa bypassed)`")
        await asyncio.sleep(2)
        await message.edit(content=f"""Found:Email: `{member.display_name}{random.choice(self.emails)}@gmail.com` Password: `{random.choice(self.passwords)}`""")
        await asyncio.sleep(2)
        await message.edit(content=f"`Fetching DMs with closest friends (if they got any of course lol)`")
        await asyncio.sleep(2)
        await message.edit(content=f"""**Last DMs**:`\"{random.choice(self.quotes)}\"`""")
        await asyncio.sleep(2)
        await message.edit(content=f"Finding most used word...")
        await asyncio.sleep(2)
        await message.edit(content=f"""mostCommon = \"{random.choice(self.randomWord)}\"""")
        await asyncio.sleep(2)
        await message.edit(content=f"Injecting the W33B5 virus into the discriminator of `{member.display_name}`")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Virus injected, Nitro stolen`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Finding IP address`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""**IPV4**:127.0.0.1, **PORT**:8080""")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Accessing Steam account...`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Changing Steam account password...`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Stealing all the games (ooo they've got some nice ones)`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Sending your search history to the FBI`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Reporting discord account for breaking TOS...`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""`Deleting System32`""")
        await asyncio.sleep(2)
        await message.edit(content=f"""Finished hacking {member.mention}, user will now be deleted ^^""")
        await asyncio.sleep(2)

    @commands.command()
    async def meme(self,ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://meme-api.herokuapp.com/gimme") as r:
                    data = await r.json()
                    embed = discord.Embed(title=f"{data['title']}")
                    embed.set_image(url=data['url'])
                    await ctx.send(embed=embed)
    @commands.command()
    async def emojify(self, ctx,*,text):
        emojis = []
        for s in text.lower():
            if s.isdecimal():
                num2emo = {'0': 'zero','1': 'one','2': 'two', '3': 'three',
                        '4': 'four', '5': 'five', '6': 'six',
                        '7': 'seven', '8': 'eight', '9': 'nine'}
                emojis.append(f":{num2emo.get(s)}:")

            elif s.isalpha():
                emojis.append(f':regional_indicator_{s}:')
            elif s == " ":
                emojis.append(" ")
            else:
                emojis.append(":sparkles:")

        await ctx.send("".join(emojis))
 
    @commands.command()
    async def docs(self, ctx):
        await ctx.send("Here is our documentation page:\nhttps://github.com/ken-soares/Yuki-chan-discordbot/blob/main/Documentation.md#Commands-List")
   
    @commands.command(aliases=['pp', 'pfp', 'pdp'])
    async def getpfp(self,ctx, member: discord.User=None):
     if not member:
      member = ctx.author
     await ctx.send(member.avatar_url)

    @commands.command()
    async def randomify(self,ctx,*,message):
        await ctx.message.delete()
        response ="**"+''.join(choice((str.upper, str.lower))(c) for c in message)+"**"
        await ctx.send(response)

    @commands.command()
    async def changelog(self, ctx):
        with open("changelog.txt", "r") as f:
            changes = f.read()
            f.close()
        Embed = discord.Embed(title="latest changes",
                description=changes,
                colour=discord.Colour.random())
        await ctx.send(embed=Embed)
   

def setup(client):
    client.add_cog(Misc(client))
