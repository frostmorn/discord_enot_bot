import discord
import json
import discord.ext
from commands import map as map_commands
from events.on_message.map_loader import map_download
from helpers import calc_sha
import os 
from discord.ext.commands import CommandNotFound
from discord.ext import commands
from helpers import load_config
# load config
config = load_config()
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