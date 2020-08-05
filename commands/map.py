from discord.ext import commands
import os
from discord.ext.commands import Cog
import textwrap
from helpers import monospace_message as monospace 
from helpers import monospace_solarized_cyan_message as monospace_cyan
from helpers import monospace_solarized_yellow_message as monospace_yellow
from helpers import monospace_solarized_green_message as monospace_green
from helpers import monospace_solarized_red_message as monospace_red
import json
import asyncio
import time

config = {}
with open("config.json") as config_file:
    config = json.load(config_file)
class Maps(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command()
    async def maps(self, ctx):
        """
            Get _FIONA_ maps list
        """
        message_list = []
        os.chdir(config["map_path"])
        files = os.listdir()
        files.sort()

        message_list.append(await ctx.send(monospace("Maps list\t:\r\nUpload Date:\t\t\tMap name:\r\n")))
        message = ""
        for file in files:
            message = message + "%s" % time.ctime(os.path.getmtime(file))+"\t"+ file +"\r\n"
            if len(message) > 1900:
                message_list.append(await ctx.send(monospace_yellow(message)))
                message = ""
        message_list.append(await ctx.send(monospace_yellow(message)))    
        message = "Count = "+str(len(files))

        message_list.append(await ctx.send(monospace_green(message)))
        try:
            await ctx.message.delete()
        except:
            pass
        await asyncio.sleep(config["map_message_time_exist"])
        for message in message_list:
            await message.delete()