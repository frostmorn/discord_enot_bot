import discord
import json
import discord.ext
import sys
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
config_file_path = "config.json"
if len(sys.argv) == 2:
    print("provided config file :\r\n", sys.argv[1])
    if os.path.isfile(sys.argv[1]):
        config_file_path = sys.argv[1]
    else:
        raise Exception("CONFIG FILE DOESN'T EXIST")
    
config = {}
with open(config_file_path) as config_file:
    config = json.load(config_file)


bot = commands.Bot(config["command_triger"])


bot.add_cog(map_commands.Maps(bot))

bot.add_cog(base_commands.Base(bot))

bot.add_cog(bot_commands.Bot(bot))
bot.add_cog(reactions_commands.Reactions(bot))
bot.add_cog(xkcd_commands.Xkcd(bot))
bot.run(config["token"])
