from discord import Colour
from discord import Embed
from discord.ext import commands
import keyw
from helpers import monospace_solarized_red_message
from helpers import monospace_message
from helpers import get_leaderboard
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
    @commands.command()
    async def gld(self, ctx, line):
        """
            Get MEE6 Leaderboard Data
        """ 

        exp_data =  get_leaderboard()
        for mention in ctx.message.mentions:
            set_exit = 0
            found = 0
            for player in exp_data["players"]:
                if set_exit:
                    break
                if int(player["id"]) == mention.id:

                    embed = Embed(title=str("Rank data for user ")+str(mention.display_name), colour=Colour(0x8CFE63))
                    embed.add_field(name="Level", value=player["level"])
                    embed.add_field(name="Messages", value=player["message_count"])
                    embed.add_field(name="EXP", value=player["xp"])
                    set_exit = 1
                    found = 1
                    await ctx.send(embed=embed)
                    break
            if not found:
                embed = Embed(title=str("Rank data for user ")+str(mention.display_name), colour=Colour(0xFF0000))
                embed.add_field(name="Rank", value="NOT_EXIST")
                await ctx.send(embed=embed)
                found = 0
