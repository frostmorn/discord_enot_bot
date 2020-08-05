import discord
import json
import discord.ext
from discord.ext import commands
from commands import map as map_commands
from commands import base as base_commands
from commands import bot as bot_commands
from commands import base

from tasks import ghost_log
from tasks import del_bot_shit
from events.on_message.map_loader import map_download
from helpers import calc_sha
import os 
from discord.ext.commands import CommandNotFound
# load config
config = {}
with open("config.json") as config_file:
    config = json.load(config_file)

bot = commands.Bot(config["command_triger"])


bot.add_cog(map_commands.Maps(bot))

bot.add_cog(base_commands.Base(bot))

bot.add_cog(bot_commands.Bot(bot))

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



bot.loop.create_task(ghost_log.file_tail(bot, config, 1))
bot.loop.create_task(del_bot_shit.del_bot_shit(bot, config, 1))

# run bot
bot.run(config["token"])
