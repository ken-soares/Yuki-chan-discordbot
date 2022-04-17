import discord
import random
from discord.ext import commands

class MiniGames(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['sus','amogus'])
    async def imposter(self,ctx):

        with open("cogs/ressources/amongus.txt", "r") as f:
            hints = f.read().split("\n")
            f.close()

        imposter = random.randint(1,3)
        dictImposter = {'cyan': 1, 'red': 2, 'yellow': 3} 

        embed1 = discord.Embed(
                title = "Vote for the imposter!",
                color = discord.Color.teal(),
                description = f"hint: {hints[random.randint(0,len(hints)-1)]}\n(cyan,yellow,red)"
                )

        embed1.set_image(url="https://i.imgur.com/jgnGPFm.png")
        await ctx.send(embed=embed1)
        responded = False
        while not responded:
            response = await self.client.wait_for('message') 
            if response.author == ctx.author:
                responded = True
                if response.content.lower() not in dictImposter.keys():
                    await ctx.send("Answer to the question you **idiot** :knife:")
                elif dictImposter[response.content.lower()] == imposter: 
                    await ctx.send(f"{response.content.lower()} was the imposter, you won!")
                else:
                    await ctx.send(f"{response.content.lower()} was not the imposter, you lose...")
            else:
                pass

    @commands.command(aliases=['rps'])
    async def rockpaperscissors(self, ctx):
        await ctx.send("rock, paper or scissors (r, p, s)?")
        responded = False
        if not responded:
            move = await self.client.wait_for('message')
            comp = random.randint(0,3)
            move = move.content.lower()
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
        else:
            responded = False

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
            responded = False
            while not responded:
                response = await self.client.wait_for('message')
                if response.author == ctx.author:
                    responded = True
                    guess = int(response.content)
                    if guess > number:
                        await ctx.send(f'the number is smaller, number of guesses:{i+1}')
                    elif guess < number:
                        await ctx.send(f'the number is bigger, number of guesses:{i+1}')
                    else:
                        await ctx.send(f'you found the number! :partying_face:')
                        break
                else:
                    responded = False
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
