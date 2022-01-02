import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Won't do the 'pong!' joke, you have a latency of {round(self.client.latency * 1000)} ms.")

    @commands.command()
    async def docs(self, ctx):
        await ctx.send("Here is our documentation page:\nLIEN DE LA DOCUMENTATION")
    
    @commands.command()
    async def changelog(self, ctx):
        with open("cogs/changelog.txt", "r") as f:
            changes = f.read()
            f.close()
        await ctx.send(f'```LATEST CHANGES:\n{changes}```')


def setup(client):
    client.add_cog(Misc(client))
