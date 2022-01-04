import discord
import pandas
import random
from discord.ext import commands

class Relationships(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def kiss(self, ctx,*, user):
        if type(user) == discord.User:
            embed = discord.Embed(
                    description = f"{ctx.message.author} kissed {user.mention}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxkiss = len(file['kiss']) - 1
            embed.set_image(url=f"{file['kiss'][random.randint(0, maxkiss)]}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                    description = f"{ctx.message.author} kissed {user}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxkiss = len(file['kiss']) - 1
            embed.set_image(url=f"{file['kiss'][random.randint(0, maxkiss)]}")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Relationships(client))
