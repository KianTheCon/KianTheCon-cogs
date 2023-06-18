from .mcstatuscheck import MCStatusCheck


async def setup(bot):
    await bot.add_cog(MCStatusCheck(bot))
