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
        try:
            status = server.status()
            latency = str(status.latency)
            SEmbed = discord.Embed(description = "```yaml\n+SERVER ONLINE+\nPlayers: {0}\nPing: {1} ms\n```".format(status.players.online, status.latency), colour=discord.Color.from_rgb(0,255,0))
        except:
            SEmbed = discord.Embed(description="```diff\n-SERVER OFFLINE-\n```", colour=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=SEmbed)

    @commands.command()
    async def players(self, ctx, server_ip: str):
        server = JavaServer.lookup(server_ip);
        SEmbed = discord.Embed(description = "```diff\n-NO PLAYERS ONLINE-\n```",colour=discord.Color.from_rgb(255,0,0))
        try:
            query = server.query()
            if query.players.names:
                SEmbed = discord.Embed(title = 'Players Online',description = "```yaml\n" + "\n".join(query.players.names) + "\n```",colour=discord.Color.from_rgb(21,244,238))
        except:
            try:
                status = server.status()
                SEmbed = discord.Embed(title = 'Players Online',description = "```yaml\n" + "\n".join([player.name for player in status.players.sample]) + "\n```",colour=discord.Color.from_rgb(21,244,238))
            except:
                SEmbed = discord.Embed(description = "```diff\n-NO PLAYERS ONLINE-\n```",colour=discord.Color.from_rgb(255,0,0))
            
        await ctx.send(embed=SEmbed)
