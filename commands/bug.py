import uuid
from discord.ext import commands
import os
from discord.ext.commands import Cog
import textwrap
from discord import Embed
from helpers import monospace_message as monospace 
from helpers import monospace_solarized_cyan_message as monospace_cyan
from helpers import monospace_solarized_yellow_message as monospace_yellow
from helpers import monospace_solarized_green_message as monospace_green
from helpers import monospace_solarized_red_message as monospace_red
from helpers import load_config
import json

import asyncio
import time
config = load_config()
class Bug(Cog):

    def bugs_save(self):
        with open(config['bug_path'], "w") as bugs_file:
            bugs = self.bugs
            json.dump(bugs, bugs_file)
            bugs_file.close()
        pass
    def bugs_read(self):


        with open(config['bug_path'], "r") as bugs_file:
            self.bugs = json.load(bugs_file)
            bugs_file.close()

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.bugs = []
        self.bugs_read()

    @commands.command()
    async def badd(self, ctx):
        
        """
            Adds bug to list
        """
        name = " ".join(ctx.message.content.split(" ")[1:])
        bug_exists = False
        for bug in self.bugs:
            if name == bug["name"]:
                bug_exists = True
                await ctx.send("Bug with name = " +name+ " allready exists with ID "+str(bug["no"])) 
        if not (bug_exists):
            self.bugs.append(   {
                                "no": uuid.uuid4().hex[:6].upper(),
                                "name":name,
                                "author":ctx.author.mention
                            } 
                        )
        self.bugs_save()
        embed = Embed(title="Bug ID "+str(self.bugs[-1]["no"]+ "[added]"))
        embed.add_field(name="Name:", value=self.bugs[-1]["name"])
        embed.add_field(name="author", value=self.bugs[-1]bug["author"])
        await ctx.send(embed=embed)
    @commands.command()
    async def brm(self, ctx, no):
        
        """
            Removes bug from list with ID
        """
        
        for bug in self.bugs:
            if no == bug["no"]:
                embed = Embed(title="Bug ID "+str(self.bugs[-1]["no"]+ "[deleted]"))
                embed.add_field(name="Name:", value=self.bugs[-1]["name"])
                embed.add_field(name="author", value=self.bugs[-1]["author"])
                await ctx.send(embed=embed)  
                self.bugs.remove(bug)
                self.bugs_save()
                return
        else:
            await ctx.send("Bug with ID " + no + " doesn't exist.") 

    @commands.command()
    async def blist(self, ctx):
        """
            Shows bugs list
        """
        for bug in self.bugs:
            embed = Embed(title="Bug ID "+str(bug["no"]))
            embed.add_field(name="Name:", value=bug["name"])
            embed.add_field(name="author", value=bug["author"])
            await ctx.send(embed=embed)
        pass

    
