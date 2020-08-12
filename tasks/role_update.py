from discord.utils import get as dget
import asyncio
import datetime
from helpers import get_leaderboard
async def role_update(bot, config, sleep_time):
    await bot.wait_until_ready()
    
    while 1:
        try:
            leaderboard = get_leaderboard()
            guild =  bot.get_guild(598903919602696202)
            players = leaderboard["players"]
            set_exit = 0
            for member in guild.members:
                for role in member.roles:
                    # If member has role Constant(743022066365890592) 
                    if role.id == 743022066365890592:
                        set_exit = 1
                        break
                if set_exit:
                    set_exit = 0
                    continue
                for player in players:
                        
                    if int(player["id"]) == member.id: 
                        if player['xp'] > 100:                              # TEST(743042483474268210)
                            if not 
                            await member.add_roles(dget(guild.roles, id = 743042483474268210)) 
                            print(player)
                        if player['xp'] < 5000:                             # Пездюк(685921321082683525)
                            await member.add_roles(dget(guild.roles, id = 685921321082683525)) 
                            pass
                        elif player['xp']> 5000 and player['xp']<10000:   # Юнлинг(598907144607367199)
                            await member.add_roles(dget(guild.roles, id =598907144607367199)) 
                            pass
                        elif player['xp']> 10000 and player['xp']<15000:  # Падаван(668752138998120448)
                            await member.add_roles(dget(guild.roles, id =668752138998120448)) 
                            pass
                        elif player['xp']> 15000 and player['xp']<20000:  # Рыцарь-Джедай (658687217694146590)
                            await member.add_roles(dget(guild.roles, id =658687217694146590)) 

            asyncio.sleep(60)
            pass
        except:
            asyncio.sleep(180)
        # user = bot.get_user(627554926314258433)
        # # user.edit(nick = "Профан Alaster")
        # nickname = "Профан Alaster"
        # user.display_name =  nickname
        # guild =  bot.get_guild(598903919602696202)
        # member =  guild.get_member(627554926314258433)
        # await member.edit(nick="НУП")

        