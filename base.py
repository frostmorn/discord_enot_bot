import discord
import json
import discord.ext
from discord.ext import commands
from commands import map as map_commands
from commands import base as base_commands
from commands import bot as bot_commands
from commands import base
from commands import xkcd as xkcd_commands
from commands import reactions as reactions_commands
from tasks import ghost_log
from tasks import del_bot_shit
from tasks import role_update
from helpers import calc_sha
from helpers import load_config
import os 
from discord.ext.commands import CommandNotFound
# load config

config = load_config()

bot = commands.Bot(config["command_triger"])


bot.add_cog(map_commands.Maps(bot))

bot.add_cog(base_commands.Base(bot))

bot.add_cog(bot_commands.Bot(bot))
bot.add_cog(reactions_commands.Reactions(bot))
bot.add_cog(xkcd_commands.Xkcd(bot))
bot.run(config["token"])
