import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self,ctx,member:discord.Member, *, reason=None):
        await ctx.send(f"Kicked {member.mention} for \"{reason}\"")
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self,ctx,member:discord.Member,*, reason=None):
        await ctx.send(f"Banned {member.mention} for \"{reason}\"")
        await member.ban(reason=reason)

def setup(client):
    client.add_cog(Moderation(client))
