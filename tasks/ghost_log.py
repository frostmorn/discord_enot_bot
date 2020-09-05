
from helpers import monospace_message as monospace 
from helpers import monospace_solarized_cyan_message as monospace_cyan
from helpers import monospace_solarized_yellow_message as monospace_yellow
from helpers import monospace_solarized_green_message as monospace_green
from helpers import monospace_solarized_red_message as monospace_red
from helpers import get_apm_data
import sys
import os
import asyncio
import discord
CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

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
        print(CRED + "[ ERROR ]" + CEND + " ghost log open error")
        return
    
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
                
                if "Online Players > " in line:

                    await bot.change_presence(activity= discord.Game(name = "WC3 "+line[line.find(">")+1:].strip()+" players"))
            
                if 'saving data to file' in line:
                    print("Replay file created")
                    replay_file = line.split("[")[3].replace("]", "").replace("\n", "").replace("\r", "")

                    await bugs_and_replays_channel.send(file=discord.File(replay_file))
                    # replay_file = 

                    embed = discord.Embed(title="Players APM:  "+replay_file, colour=discord.Colour(0x000000))
                    apm_data = get_apm_data(replay_file)
                    print(apm_data)
                    for apm_element in apm_data:
                        embed.add_field(name=apm_element["player"], value=str(apm_daapm_element["apm"]))
                        
                    await bugs_and_replays_channel.send(embed=embed)
                    # TGHISDASD ASD TODO: MAKE THAT WORK
                    # await bugs_and_replays_channel.send(get_apm_message(replay_file), file=discord.File(filename=replay_file, "Replay.w3g"))

                    
                    # [line.find("]")+1:][line.find("]")+1:][line.find("[")+2:].replace(']', '')
            await asyncio.sleep(sleep_time)

        
