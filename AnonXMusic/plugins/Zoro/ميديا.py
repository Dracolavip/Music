import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from asyncio import gather


@app.on_message(filters.command(["تلغراف", "تلغراف ميديا", "ميديا", "تلجراف", "تليجراف"]) & filters.group)
async def telegraph(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("🤕 ¦ الرد على ملف وسائط مدعوم\n• حط صوره و اكتب عليها 00")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("غير مدعوم!!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"<b>• الــرابـط:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🎯 ¦ افـتح الـرابـط", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="♻️ ¦ مشـاركه الـرابـط", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
            ]
        )
    )
    finally:
        os.remove(download_location)



