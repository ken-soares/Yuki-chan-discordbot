import discord
import random
from discord.ext import commands

class MiniGames(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['rps'])
    async def rockpaperscissors(self, ctx, move: str):
        comp = random.randint(0,3)
        move = move.lower()
        if move == 'r' or move == 'rock':
            if comp == 0:
                await ctx.send(":rock: I played rock too, it's a tie.")
            elif comp == 1:
                await ctx.send(":roll_of_paper: I played paper, I win!")
            else:
                await ctx.send(":scissors: I played scissors, you win...")
        elif move == 'p' or move == 'paper':
            if comp == 0:
                await ctx.send(":rock: I played rock, you win...")
            elif comp == 1:
                await ctx.send(":roll_of_paper: I played paper too, it's a tie.")
            else:
                await ctx.send(":scissors: I played scissors, I win!")
        else:
            if comp == 0:
                await ctx.send(":rock: I played rock, I win!")
            elif comp == 1:
                await ctx.send(":roll_of_paper: I played paper, you win...")
            else:
                await ctx.send(":scissors: I played scissors too, it's a tie")

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx):
        choices = ["heads :neutral_face:", "tails :cat2:"]
        rancoin = random.choice(choices)
        await ctx.send(rancoin)

    @commands.command()
    async def guess(self, ctx):
        number = random.randint(0, 20)
        await ctx.send('Guess the number (0-20), you have 5 guesses')
        for i in range(0, 5):
            response = await self.client.wait_for('message')
            guess = int(response.content)
            if guess > number:
                await ctx.send(f'the number is smaller, number of guesses:{i+1}')
            elif guess < number:
                await ctx.send(f'the number is bigger, number of guesses:{i+1}')
            else:
                await ctx.send(f'you found the number! :partying_face:')
                break
        await ctx.send(f"the number was {number}")

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
