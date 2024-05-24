import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonXMusic import app
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus



@app.on_message(filters.command(["رتبتي"])
    & filters.group
)
async def rotba(client, message):
    dev = (OWNER_ID)
    ze = (6753126490)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == ze:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
    elif message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــن"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    else:
         rotba = "عضــو جميل"
    await message.reply_text(f"رتبتك في هذه المجموعه \nهــي ← «{rotba}»")