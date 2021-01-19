import asyncio
import os
import uuid
from helpers import download_file
from helpers import get_apm_data
import os
from discord import Embed, Colour
from helpers import calc_sha
from helpers import download_file
async def map_download(client, config, attachment, msg):
    await client.wait_until_ready()
    os.chdir(config["map_path"])
    filename    =   attachment.filename.replace(' ', '_')
    map_name    =   filename
    old_map_sha = ""
    new_map_sha = ""

    embed = ""
    print("Filename = ", filename)
    if os.path.isfile(filename):
        old_map_sha = calc_sha(filename)
        print("File ", filename, " exist")
        new_filename = uuid.uuid4().hex[:6].upper() + "_" +filename
        print("New filename ", new_filename)
    await download_file(attachment.url, new_filename)

    if old_map_sha != "":
        new_map_sha = calc_sha(new_filename)
        if old_map_sha == new_map_sha:
            os.remove(new_filename)
            embed = Embed(title=str("Map upload error [ allready exist ] (" + str(msg.author.display_name)+")"), colour=0xff0000)
            embed.add_field(name ="MAPNAME", value = map_name)
            embed.add_field(name="SHA1SUM", value = new_map_sha)
 
        else:
            embed = Embed(title=str("Map upload [ complete  but another found ] (" + str(msg.author.display_name)+")"), colour=0x0000ff)
            embed.add_field(name ="OLD MAPNAME", value = filename)
            embed.add_field(name ="NEW MAPNAME", value = new_filename)
            embed.add_field(name="NEW SHA1SUM", value = new_map_sha)
            embed.add_field(name="OLD SHA1SUM", value = old_map_sha)

    else:
        embed = Embed(title=str("Map upload [ complete ] (" + str(msg.author.display_name)+")"), colour=0x00ff00)
        embed.add_field(name ="MAPNAME", value = filename)
    print("OLD MAP SHA1 ", old_map_sha)
    print("NEW MAP SHA1 ", new_map_sha)
    await msg.channel.send(embed = embed)
    
