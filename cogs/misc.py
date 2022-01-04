import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

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
