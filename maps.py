import discord
import json
import discord.ext
from commands import map as map_commands
from events.on_message.map_loader import map_download
from helpers import calc_sha
import os 
from discord.ext.commands import CommandNotFound
import sys

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
bot 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
@bot.event
async def on_message(message):
    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith('.w3x') or attachment.filename.endswith('.w3m'):
                await map_download(bot, config, attachment, message)
    await bot.process_commands(message)

# run bot
bot.run(config["token"])