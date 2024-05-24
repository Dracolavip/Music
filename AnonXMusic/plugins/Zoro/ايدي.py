import asyncio
import os
import time
import requests
from pyrogram import enums
import aiohttp
import datetime
from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from AnonXMusic.core.call import Anony
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait


# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# ▒▒▒▗▉████████████▅▒▒▒▒▒▗██████████▄▒▒▒▄█████████▖▒▒▒▒▒▒▒▒▒▅████████▄▒▒▒▒▒▒▒▒▒▒
# ▒▒▒▝██████████████▒▒▒▒▒███████████▀▒▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒▒██▘▒▒▒▒▒▒▝██▒▒▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▄█▄▒▒███▒▒▒▒███▘▒▒▒██▒▒▒▝███▒▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒███▒▒███▒▒▒███▒▒▒▅████▄▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▀█▀▒▒███▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒█████████▖▒▒▒▒▒██████████▀▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒█████████▘▒▒▒▒▒███████▀▀▀▒▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒███▒▒▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒▒██▉▘▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒███▒▒▒▒▒▒███▒▒▒██████▒▒▒███▒▒▒▒▒▒
# ▒▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒████▒▒▒███▒▒▒▒▒▒▒
# ▒▒▒▒▒███▘▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒███▒▒▒▒▒▒██▄▒▒▒██▒▒▒▄██▒▒▒▒▒▒▒▒
# ▒▒▒▗███████████████▅▒▒▒███████████▄▒▒▒███▒▒▒▒▒▒▒███▒▒▒▒▒▒██▖▒▒▒▒▒▒▗██▒▒▒▒▒▒▒▒▒
# ▒▒▒▀███████████████▀▒▒▒▝██████████▀▒▒▒███▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▀███████▀▒▒▒▒▒▒▒▒▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 
# (𝐂) 𝟐𝟎𝟐𝟒-𝟐𝟎𝟐𝟓 𝐛𝐲: @TopVeGa

@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""), group=95)
async def ownner(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await app.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"**المالك : {m.first_name}\nيوزر :@{m.username}\nايدي ᚐ:`{m.id}`\nشات {message.chat.title}\nايدي شات:`{message.chat.id}`",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"المالك : {m.first_name}\nيوزر :@{m.username}\nايدي ᚐ:`{m.id}`\nشات {message.chat.title}\nايدي شات:`{message.chat.id}`**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("حجي هدا ساب الدنيا و مافيها\n༄")


                

iddof = []
@app.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"], ""), group=509)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
      if message.chat.id in iddof:
        return await message.reply_text(" حجي انت تم معطل من قبل\n༄")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل الايدي بنجاح\n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك\n༄")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], ""), group=678)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
      if not message.chat.id in iddof:
        return await message.reply_text(" حجي انت الايدي مفعل من قبل\n༄ ")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح  الايدي بنجاح\n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك\n༄")




@app.on_message(filters.command(["ايدي","الايدي","ا"], ""), group=99)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""الاسم : {message.from_user.mention}\nاليوزر :  @{message.from_user.username}\nالايدي :`{message.from_user.id}`\nالبايوᚐ: {usr.bio}\nجروبᚐ: {message.chat.title}\nايدي الجروب: `{message.chat.id}`**""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    







###ترحيب

@app.on_message(filters.new_chat_members)
async def welcome(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    chat_id = message.chat.id
    egypt_tz = timezone('Egypt')
    current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = message.date.strftime("%Y-%m-%d")
    await app.send_message(chat_id=chat_id, text=f"لا تُسِئ اللفظ وإن ضَاق عليك الرَّد\nɴᴀᴍᴇ ⌯ {message.from_user.mention}\nᴜѕᴇʀɴᴀᴍᴇ ⌯ @{message.from_user.username}\n𝖣𝖺𝗍𝖾 ⌯ {date}\n𝖳𝗂𝗆𝖾 ⌯ {current_time}")



@app.on_message(filters.command("وقت انضمامي"), group=701129011)
async def timeadd(client: Client, message: Message):
    user_joined = await client.get_chat_member(message.chat.id, message.from_user.id)
    join_date = user_joined.date.strftime("%Y-%m-%d")
    join_time = user_joined.date.strftime("%H:%M:%S")
    await app.send_message(chat_id=message.chat.id, text=f"وقت انضمامك إلى المجموعة: {join_date} {join_time}")



	
	
@app.on_message(filters.left_chat_member)
async def god_bay(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    chat_id = message.chat.id
    egypt_tz = timezone('Egypt')
    current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = message.date.strftime("%Y-%m-%d")
    await app.send_message(chat_id=chat_id, text=f"وَأَن لَّيْسَ لِلْإِنسَانِ إِلَّا مَا سَعَىٰ\nɴᴀᴍᴇ ⌯ {message.from_user.mention}\nᴜѕᴇʀɴᴀᴍᴇ ⌯ @{message.from_user.username}\n𝖣𝖺𝗍𝖾 ⌯ {date}\n𝖳𝗂𝗆𝖾 ⌯ {current_time}")




       


@app.on_message(filters.command(["اسمي"], ""), group=6658)
async def vgdg(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    await message.reply_text(
        f"""** عااشت الاسامي** »» `{message.from_user.mention}`\n༄""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )