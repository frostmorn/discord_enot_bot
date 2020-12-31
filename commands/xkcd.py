from lxml import html
from discord.ext.commands import Cog
from helpers import get_request
from discord import Embed
from discord.ext import commands
from helpers import monospace_solarized_red_message as error_msg
class Xkcd(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command()
    async def xkcd(self, ctx):
        """
            Returns random xkcd comix
        """ 
        req = await get_request("https://xkcd.ru/random/")
        if req.status_code == 200:
            html_object = html.fromstring(req.content.decode("utf-8"))
            comix_img = html_object.xpath("/html/body/div/a[1]/img/@src")[0]
            print(comix_img)
            embed = Embed(title="XKCD comix")
            embed.set_image(url=comix_img)
            await ctx.send(embed=embed)
        else:
            await ctx.send(error_msg("Error happened while parsing comix"))