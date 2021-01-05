# discord_enot_bot
Discord connector for enot wc3 game hosting bot

fiona.py represents logger which gets data from enot logs, 
parse them and deliver to discord

base.py represents bot which do simple base functions,
such as kbd layout changer, xkcd comixes, etc.

maps.py represents bot which deliver maps from discord to
enot maps folder

all these bots using config file provided by argv[1]
in json format, and drops to config.json in root project
directory if it wasn't provided.

Format of that file u could find in previous commits,
all secure data provided there r just an example.

yep..
