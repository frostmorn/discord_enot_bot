import asyncio
import os
import uuid
from helpers import monospace_message as monospace 
from helpers import monospace_solarized_cyan_message as monospace_cyan
from helpers import monospace_solarized_yellow_message as monospace_yellow
from helpers import monospace_solarized_green_message as monospace_green
from helpers import monospace_solarized_red_message as monospace_red
from helpers import download_file
from helpers import get_apm_message
import os
from helpers import calc_sha
from helpers import download_file
async def map_download(client, config, attachment, msg):
    await client.wait_until_ready()
    os.chdir(config["map_path"])
    filename    =   attachment.filename.replace(' ', '_')
    extension   =   filename.split(".")
    filename    =   ".".join(extension[:len(extension)-1])
    map_name = filename
    extension   =   extension[len(extension)-1]
    old_map_sha =   ""

    if os.path.isfile(filename + "." + extension):
        old_map_sha = calc_sha(filename + "." + extension)
        filename = filename + uuid.uuid4().hex[:6].upper()
    await download_file(attachment.url, filename + "." + extension)
    if old_map_sha != "":
        new_map_sha = calc_sha(filename + "." + extension)
        if old_map_sha == new_map_sha:
            message = monospace_red("Map allready exists with name " + map_name)
            os.remove(filename + "." + extension)
        else:
            message = monospace("Map uploaded. Map name - " + filename)
    else:
        message = monospace("Map uploaded. Map name - " + filename)

    await msg.channel.send(message)
    
