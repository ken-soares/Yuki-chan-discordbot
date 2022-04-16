import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='kick',pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member, *, reason=None):
        await ctx.send(f"Kicked {member.mention} for \"{reason}\"")
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self,error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send(text)

    @commands.command(name='ban',pass_context=True)
    @commands.has_permissions(ban_members=True, manage_roles=True)
    async def ban(self,ctx,member:discord.Member,*, reason=None):
        await ctx.send(f"Banned {member.mention} for \"{reason}\"")
        await member.ban(reason=reason)

    @ban.error
    async def ban_error(self,error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send(text)

    @commands.command(name='clear',pas_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
       await ctx.channel.purge(limit=amount+1) 

    @clear.error
    async def clear_error(self,error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send(text)

    @commands.command(name='unban', pass_context=True)
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *,member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}.")
                return
    @unban.error
    async def unban_error(self,error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
            await ctx.send(text)

def setup(client):
    client.add_cog(Moderation(client))
