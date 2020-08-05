import asyncio
import os
from helpers import monospace_message as monospace 
from helpers import monospace_solarized_cyan_message as monospace_cyan
from helpers import monospace_solarized_yellow_message as monospace_yellow
from helpers import monospace_solarized_green_message as monospace_green
from helpers import monospace_solarized_red_message as monospace_red
from helpers import download_file
from helpers import get_apm_message

async def replay_parse(config, message):
    if message.attachments:
        for attachment in message.attachments:
            print(attachment)
            if attachment.filename.endswith('.w3g'):
                for role in message.author.roles:
                    if role.id == 685921321082683525:   # Пездюки
                        await message.channel.send(monospace_red("Replay parsing not supported for user with role " + role.name))
                        return
                    if role.id == 598907144607367199:   # Юнлинги
                        await message.channel.send(monospace_red("Replay parsing not supported for user with role " + role.name))
                        return

                os.chdir(config["loaded_replay_path"])
                await download_file(attachment.url, attachment.filename)
                apm_message = get_apm_message(attachment.filename)
                print(apm_message)
                await message.channel.send(apm_message)

            
            if attachment.filename.endswith('.w3x') or attachment.filename.endswith('.w3m'):
                for role in message.author.roles:
                    if role.id == 685921321082683525:   # Пездюки
                        await message.channel.send(monospace_red("Map uploading not supported for user with role " + role.name))
                        return
                os.chdir(config["map_path"])
                filename = attachment.filename.replace(' ', '_')
                current_ext = '.w3x'if attachment.filename.endswith('.w3x') else '.w3m'
                if not filename in maps_list:
                    await download_file(attachment.url, attachment.filename.replace(' ', '_'))
                    sum = calc_sha(attachment.filename.replace(' ', '_'))
                    if sum in hashes:
                        await message.channel.send(monospace_yellow("Hash compared. Looks like map allready exists, but it have a diferent name\r\nTry to use this name to host map "+maps_list[hashes.index(sum)]))
                        os.remove(filename)
                    else:
                        maps_list.append(filename)
                        hashes.append(sum)
                        await message.channel.send(monospace_green("Yau! New map detected! Uploading to bot."))
                        create_map_base_config(filename, filename.replace('.w3x', '').replace('.w3m', '')+'.cfg')
                else:
                    new_filename = filename.replace(current_ext, '') + uuid.uuid4().hex[:6].upper()+current_ext
                    await download_file(attachment.url, new_filename)
                    sum = calc_sha(new_filename)
                    if sum in hashes:
                        await message.channel.send(monospace_red("Hash compared. Looks like map allready exists with the same name"))
                        os.remove(new_filename)
                    else:
                        await message.channel.send(monospace_solarized_yellow_message("Hash compared. Looks like maps are different. \r\nsha1sum of loaded map = "+sum+'\r\nSaved with name = '+new_filename))
                        create_map_base_config(new_filename, new_filename.replace('.w3x', '').replace('.w3m', '')+'.cfg')
