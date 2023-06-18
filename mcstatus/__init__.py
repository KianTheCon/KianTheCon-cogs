from .mcstatus import MCStatus


async def setup(bot):
    await bot.add_cog(MyCog(bot))
