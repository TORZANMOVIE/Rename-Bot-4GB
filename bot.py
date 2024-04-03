from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *



bot = Client(

           "Renamer",

           bot_token=BOT_TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))


if STRING:
    apps = [Client2,bot]
    print(4Gb boooy")
    for app in apps:
        app.start()
        me = app.get_me()
        prine(me.username)
    idle()
    for app in apps:
        app.stop()

else:
    print("2GB only")
    bot.run()
    

# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
