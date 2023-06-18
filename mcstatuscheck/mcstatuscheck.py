from redbot.core import commands
import discord
from mcstatus import JavaServer

class MCStatusCheck(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx, server_ip: str):
        """This does stuff!"""
        # Your code will go here
        server = JavaServer.lookup(server_ip);
        latency = server.ping()
        print(f"The server replied in {latency} ms")
        SEmbed = discord.Embed(title = 'Players Online',description = "```yaml\n" + str(latency) + "\n```",colour=discord.Color.from_rgb(21,244,238))
        await ctx.send(f"The server replied in {latency} ms")
