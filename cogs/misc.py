import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

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
        await ctx.send("Here is our documentation page:\nLIEN DE LA DOCUMENTATION")
    
    @commands.command()
    async def changelog(self, ctx):
        with open("changelog.txt", "r") as f:
            changes = f.read()
            f.close()
        await ctx.send(f'```LATEST CHANGES:\n{changes}```')


def setup(client):
    client.add_cog(Misc(client))
