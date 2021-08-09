import discord
from discord.ext import commands

class code(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def ecode(self, ctx):
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        #await ctx.send(message.content)
        with open('text.txt', 'w') as f:
            f.write(message.content)
        embed1 = discord.Embed(
            description=f"{message.content}",
            colour=discord.Color.from_rgb(183,142,255)
        )
        await ctx.send(embed=embed1)
    @commands.command()
    async def code(self, ctx):
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        with open('text.txt', 'w') as f:
            f.write(message.content)
        await ctx.send(message.content)

def setup(client):
    client.add_cog(code(client))