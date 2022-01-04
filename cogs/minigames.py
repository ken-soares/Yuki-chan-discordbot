import discord
import random
from discord.ext import commands

class MiniGames(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['8ball', 'mb'])
    async def destiny(self,ctx, *args):

        with open("cogs/ressources/responses.txt", "r") as f:
            possible_answers = f.read().split("\n")
            f.close() 

        question = " ".join(args[:])
        if question[0].isupper() and question[len(question)-1] == "?":
            await ctx.send(possible_answers[random.randint(0, len(possible_answers)-1)])
        else:
            await ctx.send(f"A proper question starts with an uppercase letter and ends with a question mark.")

def setup(client):
    client.add_cog(MiniGames(client))
