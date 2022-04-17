import discord
import pandas
import random
import aiohttp
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

    @commands.command()
    async def slap(self, ctx,*, user):
        if type(user) == discord.User:
            embed = discord.Embed(
                    description = f"{ctx.message.author} slapped {user.mention}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxslap = len(file['slap']) - 1
            embed.set_image(url=f"{file['slap'][random.randint(0, maxslap)]}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                    description = f"{ctx.message.author} slapped {user}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxslap = len(file['slap']) - 1
            embed.set_image(url=f"{file['slap'][random.randint(0, maxslap)]}")
            await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx):
        embed = discord.Embed(
                description = f"{ctx.message.author} cries",
                colour = discord.Colour.purple()
                )

        file = pandas.read_csv("cogs/ressources/relationships.csv")
        maxcry = len(file['cry']) - 1
        embed.set_image(url=f"{file['cry'][random.randint(0, maxcry)]}")
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx,*, user):
        if type(user) == discord.User:
            embed = discord.Embed(
                    description = f"{ctx.message.author} gave a headpat to {user.mention}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxpat = len(file['pat']) - 1
            embed.set_image(url=f"{file['pat'][random.randint(0, maxpat)]}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                    description = f"{ctx.message.author} gave a headpat to {user}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxpat = len(file['pat']) - 1
            embed.set_image(url=f"{file['pat'][random.randint(0, maxpat)]}")
            await ctx.send(embed=embed)
    
    @commands.command()
    async def hug(self, ctx,*, user):
        if type(user) == discord.User:
            embed = discord.Embed(
                    description = f"{ctx.message.author} hugged {user.mention}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxhug = len(file['hug']) - 1
            embed.set_image(url=f"{file['hug'][random.randint(0, maxhug)]}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                    description = f"{ctx.message.author} hugged {user}",
                    colour = discord.Colour.purple()
                    )

            file = pandas.read_csv("cogs/ressources/relationships.csv")
            maxhug = len(file['hug']) - 1
            embed.set_image(url=f"{file['hug'][random.randint(0, maxhug)]}")
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Relationships(client))
