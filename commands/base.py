import sympy
from helpers import get_request
from discord import Colour
from discord import Embed
from discord.utils import get
import discord
from discord.ext import commands
from discord.ext.commands import Cog
import keyw
from lxml import html
from helpers import monospace_message
from helpers import monospace_solarized_red_message as error_msg
import json
import sys
config = {}
with open("config.json") as config_file:
    config = json.load(config_file)
class Base(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command()
    async def echo(self, ctx, line):
        """
            Simple echo command
        """ 
        await ctx.send(line)
        await ctx.message.delete()
    @commands.command()
    async def er(self, ctx):
        """
            Last message convert from english to russian layout
        """
        translated_message =""
        embed = Embed(title=str("Message Layout Translated( :flag_us:    --->    :flag_ru:  from: ")+str(ctx.message.author.display_name)+")", colour=Colour(0x000000))
        messages = await ctx.history(limit=2).flatten()
        message = messages[1]
        splitted_message = message.content.split(" ")
        for part in splitted_message:
            if not ("<" in part and ">" in part):
                translated_message = translated_message +" "+keyw.engrus(part)
            else:
                translated_message = translated_message +" "+part

        embed.add_field(name="Message", value=translated_message)
        await ctx.send(embed=embed)
        await ctx.message.delete()    
        if message.author.id == ctx.message.author.id:
            await message.delete()

    @commands.command()
    async def re(self, ctx):
        """
            Last message convert from russian to english layout
        """
        translated_message =""
        embed = Embed(title=str("Message Layout Translated( :flag_ru:    --->    :flag_us:  from: ")+str(ctx.message.author.display_name)+")", colour=Colour(0x000000))
        messages = await ctx.history(limit=2).flatten()
        message = messages[1]
        splitted_message = message.content.split(" ")
        for part in splitted_message:
            if not ("<" in part and ">" in part):
                translated_message = translated_message +" "+keyw.ruseng(part)
            else:
                translated_message = translated_message +" "+part
        
        embed.add_field(name="Message", value=translated_message)
        await ctx.send(embed=embed)
        await ctx.message.delete()    
        if message.author.id == ctx.message.author.id:
            await message.delete()

    @commands.command()
    async def rm(self, ctx, count):
        """
            Removes last `count` of messages from chat
        """
        if ctx.author.id  == 809740190402478080 or ctx.author.id == 478639649435418628:
            messages = await ctx.history(limit=int(count)).flatten()
            for message in messages:
                try:
                    await message.delete()
                except:
                    pass
        else:
            await ctx.send("Nice try bitch")
    @commands.command()
    async def gl(self, ctx):
        """
            Get last message as quote
        """
        messages = await ctx.history(limit=2).flatten()
        message = messages[1]
        await ctx.send(monospace_message(message.content))
    @commands.command()
    async def te(self, ctx, message):
        """
            Converts text to emoji's
        """
        message = ctx.message.clean_content[ctx.message.content.find(message):]

        embed = Embed(title=str("Message Translated(from: ")+str(ctx.message.author.display_name)+")", colour=Colour(0x000000))
        new_message= ""
        skip = 0
        for character in message:
            if  ("<" == character or character == ">"):
                continue
            if skip ==1:
                if character!=" ":
                    new_message = new_message + character
                    continue
                else:

                    skip = 0
            if character == "?":
                new_message = new_message + ":question:"
            elif character == "!":
                new_message = new_message + ":exclamation:"
            elif character in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                new_message = new_message + ":regional_indicator_"+character.lower()+":"
            elif character == " ":
                new_message = new_message + "<:space:818564646762971147>"
            elif character == "@":
                new_message = new_message + " @"
                skip =1
            elif character == "0":
                new_message = new_message + ":zero:"
            elif character == "1":
                new_message = new_message + ":one:"
            elif character == "2":
                new_message = new_message + ":two:"
            elif character == "3":
                new_message = new_message + ":three:"
            elif character == "4":
                new_message = new_message + ":four:"
            elif character == "5":
                new_message = new_message + ":five:"
            elif character == "6":
                new_message = new_message + ":six:"
            elif character == "7":
                new_message = new_message + ":seven:"
            elif character == "8":
                new_message = new_message + ":eight:"
            elif character == "9":
                new_message = new_message + ":nine:"
            else:
                new_message = new_message + ""+character
                
                new_message = new_message +""
        await ctx.message.delete()

        embed.add_field(name="Message", value=new_message)
        await ctx.send(embed=embed)


    @commands.command()
    async def kick(self, ctx, user):
        """
            Kicks @username from guild
        """
        if ctx.author.id  == 566918071097360384 or ctx.author.id == 727528968504213507:        
            for mentioned_user in ctx.message.mentions:
                try:
                    await mentioned_user.kick()
                    await ctx.send("Ха-ха-ха, "+str(mentioned_user)+" kicked.")
                except discord.Forbidden:
                    await ctx.send("<@!"+str(mentioned_user.id)+"> can't be kicked due to Missing Permissions error")
                pass

        else:
            await ctx.send("You r not authorized to perform that operation. GTFO")
        pass
    @commands.command()
    async def ban(self, ctx, user):
        """
            Bans @username in guild
        """
        if ctx.author.id  == 478639649435418628 or ctx.author.id == 727528968504213507:        
            for mentioned_user in ctx.message.mentions:
                try:
                    await mentioned_user.ban()
                    await ctx.send("Ха-ха-ха, "+str(mentioned_user)+" banned.")
                except discord.Forbidden:
                    await ctx.send("<@!"+str(mentioned_user.id)+"> can't be banned due to Missing Permissions error")
                pass

        else:
            await ctx.send("You r not authorized to perform that operation. GTFO")
        pass


    @commands.command()
    async def up(self, ctx, line):
        """
            Lvlups user
        """ 
        message = ""
        
        for mentioned_user in ctx.message.mentions:
            for role in mentioned_user.roles:
                if role.id in config["roles_by_lvl"]:
                    message = message + role.name + "\r\n"
                                    
                    role_id = config["roles_by_lvl"][config["roles_by_lvl"].index(role.id)+1]
                    role = get(ctx.guild.roles, id=role_id)
                try:
                    try:
                        await mentioned_user.add_roles(role_id, "Cause "+ctx.message.author.name+" wanted that.")
                        await ctx.send(monospace_message(message))
                    except discord.NotFound:
                        await ctx.send("Unknown role I want to gave, but way I want I haven't made.")
                except discord.Forbidden:
                    await ctx.send("<@!"+str(mentioned_user.id)+"> can't be lvl upped due to Missing Permissions error")

                
        await ctx.send(monospace_message(message))

    @commands.command()
    async def gr(self, ctx, line):
        """
            Get roles for all users in mentions
        """ 
        
        for mention in ctx.message.mentions:
            embed = Embed(title=str("User ")+str(mention.display_name), colour=Colour(0x000000))
            roles = ""    
            for role in mention.roles:
                roles = roles + role.name + "\r\n"
            embed.add_field(name="Roles", value=monospace_message(roles))
        await ctx.send(embed=embed)

    @commands.command()
    async def gw(self, ctx, line):
        """
            Gets weather in `city`
        """ 
        req = await get_request("https://sinoptik.ua/погода-"+line)
        if req.status_code == 200:
            html_object = html.fromstring(req.content.decode("utf-8"))
            region = html_object.xpath("//*[@class='currentRegion']/text()")[0]
            temperature = html_object.xpath("//*[@class='today-temp']/text()")[0]
            print(temperature)
            embed = Embed(title="Weather in "+region)
            embed.add_field(name ="Temperature", value = temperature)
            await ctx.send(embed=embed)
        else:
            await ctx.send(error_msg("Error while getting weather in "+line))

    @commands.command()
    async def calc(self, ctx, line):
        """
            Computes math expression
        """ 
        expression = " ".join(ctx.message.clean_content.split(" ")[1:])
        embed = Embed(title = "Expression "+expression)
        embed.add_field(name="Value", value = str(sympy.sympify(expression)))
        await ctx.send(embed=embed)