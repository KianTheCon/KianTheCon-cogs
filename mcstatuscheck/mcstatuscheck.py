from redbot.core import commands
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
        await ctx.send(f"The server replied in {latency} ms")
