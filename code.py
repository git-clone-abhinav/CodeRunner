import discord
from discord.ext import commands
import runner

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

        f.close()
        embed1 = discord.Embed(
            description=f"{message.content}",
            colour=discord.Color.from_rgb(183,142,255)
        )
        await ctx.send(embed=embed1)

    @commands.command()
    async def code(self, ctx):
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        #print(message.content)
        with open('text.txt', 'w') as f:
            f.write(message.content)
        f.close()
        output = runner.run()
        output = str(output).lstrip("b'").rstrip("\r\n'")
        embed1 = discord.Embed(title = "CodeRunner",
            description=f"{output}",
            colour=discord.Color.from_rgb(140,194,255)
        )
        await ctx.send(embed=embed1)

        #await ctx.send(message.content)

def setup(client):
    client.add_cog(code(client))