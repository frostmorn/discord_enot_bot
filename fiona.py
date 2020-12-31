import discord
import json
import discord.ext
from discord.ext import commands
from tasks import ghost_log
import os 
import sys
from discord.ext.commands import CommandNotFound
# load config
config_file = "config.json"
if len(sys.argv) == 2:
    print("provided config file :\r\n", sys.argv[1])
    if os.path.isfile(sys.argv[1]):
        config_file = sys.argv[1]
    else:
        raise Exception("CONFIG FILE DOESN'T EXIST")
    
config = {}
with open("config.json") as config_file:
    config = json.load(config_file)

bot = commands.Bot(config["command_triger"])



bot.loop.create_task(ghost_log.file_tail(bot, config, 1))

# run bot
bot.run(config["token"])
