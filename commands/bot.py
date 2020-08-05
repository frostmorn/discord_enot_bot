from discord.ext import commands
import keyw
from helpers import monospace_message
import json
from discord.ext.commands import Cog

config = {}
with open("config.json") as config_file:
    config = json.load(config_file)
class Bot(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command()
    async def no_command(self, ctx, line):
        """
            Simple echo command
        """ 
        await ctx.send(line)
        await ctx.message.delete()
