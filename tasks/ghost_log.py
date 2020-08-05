from helpers import monospace_message as monospace 
from helpers import monospace_solarized_cyan_message as monospace_cyan
from helpers import monospace_solarized_yellow_message as monospace_yellow
from helpers import monospace_solarized_green_message as monospace_green
from helpers import monospace_solarized_red_message as monospace_red
from helpers import get_apm_message
import sys
import os
import asyncio
import discord
async def file_tail(bot, config, sleep_time):
    filename = config["ghost_log"]

    await bot.wait_until_ready()
    flood_channel = bot.get_channel(config["channels"]["flood"])
    log_channel = bot.get_channel(config["channels"]["log"])
    bugs_and_replays_channel = bot.get_channel(config["channels"]["bugs_and_replays"])
    try:
        file = open(filename, 'r', encoding='utf-8')
    except IOError:
        # sys.exit("FATAL ERROR: There was a problem opening \"{}\".".format(filename))
        print("Error with opening ghost_log occured")
    
    file.seek(0, os.SEEK_END)
    print("------")
    print("Tailing {} every {} seconds.".format(filename, sleep_time))
    
    while not bot.is_closed():
        try:
            await asyncio.sleep(sleep_time)
            lines = file.readlines()
        except UnicodeDecodeError:
            print("Encountered unknown character in server log, skipping lines.")
        else:
            for line in lines:    # Not EOF

                # if not "Watched user" in line:
                #     await log_channel.send(monospace(line))
                # replay_file = line
                if 'saving data to file' in line:
                    print("Replay file created")

                    replay_file = line.split("[")[3].replace("]", "").replace("\n", "").replace("\r", "")

                    await bugs_and_replays_channel.send(file=discord.File(replay_file))
                    # replay_file = 
                    await bugs_and_replays_channel.send(get_apm_message(replay_file))
                    # TGHISDASD ASD TODO: MAKE THAT WORK
                    # await bugs_and_replays_channel.send(get_apm_message(replay_file), file=discord.File(filename=replay_file, "Replay.w3g"))

                    
                    # [line.find("]")+1:][line.find("]")+1:][line.find("[")+2:].replace(']', '')
                   
                elif "[GHOST] creating game" in line:
                    await flood_channel.send(monospace_green(line))

                await asyncio.sleep(sleep_time)

        