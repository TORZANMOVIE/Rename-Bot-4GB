from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 20  
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 40  
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 100  
	
	
        Payment To Admin @FREEKZZ_2008"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/calladminrobot")], 
        			[InlineKeyboardButton("Phone Pay",url = "https://telegra.ph/file/7f959437f9375b313ed1c.jpg"),
        			InlineKeyboardButton("Paytm Wallet/UPI",url = "https://telegra.ph/file/30b3e45a02766803883cb.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 20
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 40
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 100  
	 
        Payment To Admin @FREEKZZ_2008"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/calladminrobot")], 
        			[InlineKeyboardButton("Phone Pay",url = "https://telegra.ph/file/7f959437f9375b313ed1c.jpg"),
        			InlineKeyboardButton("Paytm Wallet/UPI",url = "https://telegra.ph/file/30b3e45a02766803883cb.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
