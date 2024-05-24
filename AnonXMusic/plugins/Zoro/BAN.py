import asyncio
import requests
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import set_loop
from AnonXMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from config import BANNED_USERS, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
import os
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.errors import PeerIdInvalid
from os import getenv
from AnonXMusic.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv
from AnonXMusic.utils.database import (set_cmode,get_assistant) 
from AnonXMusic.utils.decorators.admins import AdminActual
from AnonXMusic import app
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)
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

muttof = []
@app.on_message(filters.command(["قفل التقيد", "تعطيل التقيد"], ""), group=419)
async def muttlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
      if message.chat.id in muttof:
        return await message.reply_text("تم قفل التقيد من قبل\n༄")
      muttof.append(message.chat.id)
      return await message.reply_text("تم تعطيل التقيد بنجاح \n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك \n༄")

@app.on_message(filters.command(["فتح التقيد", "تفعيل التقيد"], ""), group=424)
async def muttopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
      if not message.chat.id in muttof:
        return await message.reply_text("التقيد مفعل من قبل \n༄")
      muttof.remove(message.chat.id)
      return await message.reply_text("تم فتح التقيد بنجاح \n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك \n༄")
        
        
@app.on_message(filters.command(["الغاء تقيد","الغاء التقيد"], ""), group=94) 
async def mute(client: Client, message: Message):
   global restricted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
    if message.chat.id in muttof:
      return   	   	
    await app.restrict_chat_member(
                       chat_id=message.chat.id,
                       user_id=message.reply_to_message.from_user.id,
                       permissions=unmute_permissions,
                   )
    await app.send_message(message.chat.id, f" {message.reply_to_message.from_user.mention}\nابشر الغيت تقييدته\n༄ ")
   else:
         await message.reply_text(f"حجي هذا الامر ليس لك \n༄")


restricted_users = []
@app.on_message(filters.command(["تقيد"], ""), group=62)
async def mute(client: Client, message: Message):
    global restricted_users
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
        if message.chat.id in muttof:
            return
        if message.reply_to_message.from_user.id == 6909581339:
            await app.send_message(message.chat.id, "حجي لا يمكن تقيد مطور فيجا\n༄")
        else:
            mute_permission = ChatPermissions(can_send_messages=False)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=mute_permission,
            )
            restricted_user = message.reply_to_message.from_user
            restricted_users.append(restricted_user)
            await app.send_message(message.chat.id, f" {restricted_user.mention}\nقييدته\n༄ ")
    else:
         await message.reply_text(f"حجي هذا الامر ليس لك \n༄")




@app.on_message(filters.command(["مسح المقيدين"], ""), group=40)
async def unmute(client: Client, message: Message):
    global restricted_users
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 5675627801 or message.from_user.id == 6909581339:
        count = len(restricted_users)
        for user in restricted_users:
            await client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user.id,
                permissions=unmute_permissions,
            )
        restricted_users = []
        await message.reply_text(f"↢ تم مسح {count} من المقيدين")
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")
    

@app.on_message(filters.command(["المقيدين"], ""), group=13100920)
async def get_restr_users(client: Client, message: Message):
    global restricted_users
    count = len(restricted_users)
    X = 0
    user_ids = [str(user.id) for user in restricted_users]
    response = f"قائمة المقيدين وعددهم: {count}\n"
    response += "⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴀ♪\n"
    response += "\n".join(f"{X+i+1}. {user_id}" for i, user_id in enumerate(user_ids))
    await message.reply_text(response)



gaaof = []
@app.on_message(filters.command(["تعطيل الحظر", "تعطيل الطرد"], ""), group=504)
async def gaalock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in gaaof:
        return await message.reply_text("حجي الامر معطل من قبل\n༄")
      gaaof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الحظر بنجاح\n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك \n༄")

@app.on_message(filters.command(["فتح الطرد", "تفعيل الطرد", "تفعيل الحظر"], ""), group=412)
async def gaaopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in gaaof:
        return await message.reply_text("حجي الحظر مفعل من قبل\n༄")
      gaaof.remove(message.chat.id)
      return await message.reply_text("تم فتح الطرد و الحظر بنجاح\n༄")
   else:
      return await message.reply_text("حجي هذا الامر ليس لك \n༄")


        
banned_users = []
@app.on_message(filters.command(["حظر"], ""), group=39)
async def mute(client: Client, message: Message):
   global banned_users    
   chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
    if message.chat.id in gaaof:
        return
    if message.reply_to_message.from_user.id == 6909581339:
        await app.send_message(message.chat.id, "ايش تسوي انت هذا مطور السورس\n༄")
    else:
        banned_user = message.reply_to_message.from_user
        banned_users.append(banned_user)
        await app.ban_chat_member(message.chat.id, banned_user.id)
        await app.send_message(message.chat.id, f"  {banned_user.mention}\nحظرته\n༄ ")
   else:
         await message.reply_text(f"حجي هذا الامر ليس لك \n༄")

@app.on_message(filters.command(["مسح المحظورين"], ""), group=19)
async def unban_all(client: Client, message: Message):
   usr = await client.get_chat(message.from_user.id)
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
    global banned_users
    count = len(banned_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in banned_users.copy():
        user_id = member.id
        try:
            await client.unban_chat_member(chat_id, user_id)
            banned_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من المحظورين\n༄")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين محظورين ليتم مسحهم\n༄")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count}\nمن المحظورين\n༄")
   else:
         await message.reply_text(f"حجي هذا الامر ليس لك \n༄")
      
                
        
@app.on_message(filters.command(["الغاء حظر","/unban"], ""), group=42)
async def unmutegy(client: Client, message: Message):
    global banned_users
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 5675627801 or message.from_user.id == 6909581339:
        if not message.reply_to_message:
            return await message.reply_text("يجب الرد على الشخص الذي تريد إلغاء حظره")
        user = message.reply_to_message.from_user
        await app.unban_chat_member(message.chat.id, user.id)
        banned_users.remove(user)
        await app.send_message(message.chat.id, f"✅ ¦ تـم الغاء الحظر بـنجـاح\n {user.mention} ")
        


@app.on_message(filters.command(["المحظورين"], ""), group=17389336)
async def get_restricted_users(client: Client, message: Message):
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
         global banned_users
         count = len(banned_users)
         user_ids = [str(user.id) for user in banned_users]
         response = f" <u>قائمة المحظورين وعددهم :</u> {count}\n"
         response += "⭓━⭓⭓⭓⭓━⭓\n"
         response += "\n".join(user_ids)
         await message.reply_text(response)
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")





muted_users = []
@app.on_message(filters.command(["كتم"], ""), group=39)
async def mute_user(client, message):
    global muted_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:    
        if message.reply_to_message.from_user.id == 6909581339:
            await app.send_message(message.chat.id, "عذرا لا يمكنك كتم المطور فيجا")
        else:	
         if message.reply_to_message:
           user_id = message.reply_to_message.from_user.mention
         if user_id not in muted_users:
            muted_users.append(user_id)
            await message.reply_text(f" {user_id}\nكتمته\n༄")
         else:
           await message.reply_text(f"{user_id}\nمكتوم  من قبل\n༄")
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")


@app.on_message(filters.command(["الغاء الكتم"], ""), group=62)
async def unmute_user(client, message):
   global muted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:	
    user_id = message.reply_to_message.from_user.mention
    if user_id in muted_users:
        muted_users.remove(user_id)
        await message.reply_text(f" {user_id}\nابشر الغيت كتمه\n༄")
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")    
       
        
        
       
@app.on_message(filters.text)
async def handle_message(client, message):
    if message.from_user and message.from_user.mention in muted_users:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)

@app.on_message(filters.command(["المكتومين"], ""), group=137)
async def get_rmuted_users(client, message):
    global muted_users
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
         count = len(muted_users)
         user_ids = [str(user) for user in muted_users]
         response = f" <u>قائمة المكتومين وعددهم :</u> {count}\n"
         response += "⭓━⭓⭓⭓⭓━⭓\n"
         response += "\n".join(user_ids)
         await message.reply_text(response)
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")



@app.on_message(filters.command(["مسح المكتومين"], ""), group=136)
async def unmute_all(client, message):
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
    global muted_users
    count = len(muted_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in muted_users.copy():
        user_id = member
        try:
            muted_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من المكتومين\n༄")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين مكتومين ليتم مسحهم\n༄")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count}\nمن المكتومين\n༄")
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")                                  