import discord
from discord.utils import get
import asyncio
import datetime
import random

async def del_bot_shit(bot, config, sleep_time):
    await bot.wait_until_ready()
    while 1:
        try:
            now = datetime.datetime.utcnow() 
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    messages = await channel.history(limit=10).flatten()
                    for message in messages:
                        # need to add check for embed in messages
                        if (now - message.created_at).total_seconds() > 20 and message.channel.id != config['channels']['bugs_and_replays']: 
                            if hasattr(message.author, 'roles'):
                                for role in message.author.roles:
                                    if role.id == 685921321082683525 and message.channel.id != 688766751638552605:
                                        await message.delete()
                            if message.author.id == 159985870458322944 and not "http" in message.content:
                                await message.delete()
                                print(now, message.created_at)
                            if message.content[:1] == "!":
                                await message.delete()
                            if message.author.id == 234395307759108106:
                                await message.delete()
                            if message.content[:1] == "-":
                                await message.delete()
                                
            await asyncio.sleep(10)
        except:
            pass

        # user = bot.get_user(627554926314258433)
        # # user.edit(nick = "Профан Alaster")
        # nickname = "Профан Alaster"
        # user.display_name =  nickname
        guild =  bot.get_guild(598903919602696202)
        member =  guild.get_member(524429275919810561)
        
            # user.edit(nick = )
        nick= random.choice(["Говно", "залупа", "пенис", "хер", "давалка", "хуй", "блядина"
        "Головка", "шлюха", "жопа", "член", "еблан", "петух" "мудила",
        "Рукоблуд", "ссанина", "очко", "блядун", "вагина",
        "Сука", "ебланище", "влагалище", "пердун", "дрочила",
        "Пидор", "пизда", "туз", "малафья",
        "Гомик", "мудила", "пилотка", "манда",
        "Анус", "вагина", "путана", "педрила",
        "Шалава", "хуила", "мошонка", "елда"])
        await user.edit(nick =nick )
        # await member.edit(nick="НУП")

        