from discord.ext import commands
from templatebot.discordplus import commandsplus


class FunCog(commands.Cog):
    """Commands for fun."""

    def __init__(self, bot):
        self.bot = bot

    @commandsplus.command(
        hidden = True
    )
    @commands.is_owner()
    async def say(self, ctx, *, message: str):
        await ctx.message.delete(delay=0)
        await ctx.send(message)


def setup(bot):
    bot.add_cog(FunCog(bot))
