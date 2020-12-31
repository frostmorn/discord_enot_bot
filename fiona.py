import discord
import json
import discord.ext
from discord.ext import commands
from commands import map as map_commands
from commands import base as base_commands
from commands import bot as bot_commands
from commands import base
from commands import reactions as reactions_commands
from tasks import ghost_log
from tasks import del_bot_shit
from tasks import role_update
from events.on_message.map_loader import map_download
from helpers import calc_sha
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


# bot.add_cog(map_commands.Maps(bot))

# bot.add_cog(base_commands.Base(bot))

# bot.add_cog(bot_commands.Bot(bot))
# bot.add_cog(reactions_commands.Reactions(bot))
# bot 
# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, CommandNotFound):
#         return
#     raise error
# @bot.event
# async def on_message(message):
#     if message.attachments:
#         for attachment in message.attachments:
#             if attachment.filename.endswith('.w3x') or attachment.filename.endswith('.w3m'):
#                 await map_download(bot, config, attachment, message)
#     await bot.process_commands(message)



bot.loop.create_task(ghost_log.file_tail(bot, config, 1))
# bot.loop.create_task(del_bot_shit.del_bot_shit(bot, config, 1))
# bot.loop.create_task(role_update.role_update(bot, config, 1))

# run bot
bot.run(config["token"])
