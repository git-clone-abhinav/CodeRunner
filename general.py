import discord
from discord.ext import commands

class general(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=['speed','connection'])
    async def ping(self, ctx):
        embed1 = discord.Embed(
            description=f":eyes: {round(self.client.latency * 1000)} ms",
            colour=discord.Color.from_rgb(183,142,255)
        )
        await ctx.send(embed=embed1)

def setup(client):
    client.add_cog(general(client))