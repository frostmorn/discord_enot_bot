import random
from discord import Colour
from discord import Embed
from discord.ext import commands
import keyw
from helpers import monospace_message
import json
from discord.ext.commands import Cog

config = {}
with open("config.json") as config_file:
    config = json.load(config_file)
class Reactions(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command()
    async def kiss(self, ctx, user):
        """
            Kiss user
        """ 
        for mentioned_user in ctx.message.mentions:
            embed = Embed(title=str(ctx.message.author)+" kissed "+str(mentioned_user), colour=Colour(0xE5E242))
            embed.set_image(url=random.choice(config["reactions"]["kiss"]))
            await ctx.send(embed=embed)
    @commands.command()
    async def slap(self, ctx, user):
        """
            Slap user
        """ 
        for mentioned_user in ctx.message.mentions:
            embed = Embed(title=str(ctx.message.author)+" slaps "+str(mentioned_user), colour=Colour(0xE5E242))
            embed.set_image(url=random.choice(config["reactions"]["slap"]))
            await ctx.send(embed=embed)
