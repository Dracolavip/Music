import platform
import re
import socket
import uuid
import os
import speedtest
import asyncio
import platform
import asyncio

import time
import requests
from sys import version as pyver
from datetime import datetime

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver

import config
from config import OWNER_ID
from AnonXMusic import YouTube, app
from AnonXMusic import app as Client
from AnonXMusic.core.userbot import assistants
from AnonXMusic.misc import SUDOERS, mongodb
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AnonXMusic.utils.decorators.language import language, languageCB
from AnonXMusic.utils.inline.stats import back_stats_buttons, stats_buttons


import asyncio
from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import enums
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint


loop = asyncio.get_running_loop()

# Commands

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




def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID



REPLY_MESSAGE = "**صل علي نبينا محمد ﷺ**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("سورس"),
    ],
    [
       ("مطور"),
      ("مطور السورس")
    ],
    [
        ("صور شباب"),
        ("صور بنات")
    ],
    [
        ("استوري")
    ],
    [
        ("قران"),
        ("اذكار")
    ],
    [
        ("كت"),
        ("تويت")

    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي")
    ],
    [
        ("صوره"),
        ("صور انمي")
    ],
    [
        ("متحركه")
    ],
    [    
        ("بوت"),
        ("انصحني")

    ],
    [
        ("نكت"),
        ("اسال")
    ],
    [
     
        ("احكام"),
        ("صراحه")
    ],
    [
        ("قفل الكيبورد")
    ]
]

@app.on_message(filters.regex("^/start"), group=101098)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("^قفل الكيبورد"), group=5870)
async def down(client, message):
          m = await message.reply(" **تـم قـفل الكيـبورد بنـجاح\nلظهار الكيب دوس /start**", reply_markup= ReplyKeyboardRemove(selective=True))
          







# @app.on_message(filters.command(["غني","غنيلي"], ""), group=765432)
# async def ihppd(client: Client, message: Message):
    # rl = random.randint(2,90)
    # url = f"https://t.me/gukygn/{rl}"
    # await client.send_voice(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار الاغـنـية لك من استار" ,parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )


# @app.on_message(filters.command(["صوره","صورة"], ""), group=54356)
# async def ihssd(client: Client, message: Message):
    # rl = random.randint(2,50)
    # url = f"https://t.me/vnnkli/{rl}"
    # await client.send_photo(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار صوره لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )



# @app.on_message(filters.command(["متحركه"], ""), group=5090)
# async def ihqwd(client: Client, message: Message):
    # rl = random.randint(2,90)
    # url = f"https://t.me/GifWaTaN/{rl}"
    # await client.send_animation(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار ملصق لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["اقتباس","اقتباسات"], ""), group=30605)
# async def ihjnd(client: Client, message: Message):
    # rl = random.randint(2,90)
    # url = f"https://t.me/LoreBots9/{rl}"
    # await client.send_photo(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار اقتباس لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["هيدرا","هيدرات"], ""), group=4433)
# async def ihybd(client: Client, message: Message):
    # rl = random.randint(2,90)
    # url = f"https://t.me/flflfldld/{rl}"
    # await client.send_photo(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار هيدرات لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["صور بنات"], ""), group=67899)
# async def irrhd(client: Client, message: Message):
    # rl = random.randint(2,90)
    # url = f"https://t.me/vvyuol/{rl}"
    # await client.send_photo(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار صوره لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["صور شباب"], ""), group=2345)
# async def ihdyu(client: Client, message: Message):
    # rl = random.randint(2,90)
    # url = f"https://t.me/vgbmm/{rl}"
    # await client.send_photo(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار صوره لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["قران","القرآن"], ""), group=5670)
# async def ihdh(client: Client, message: Message):
    # rl = random.randint(1,90)
    # url = f"https://t.me/opuml/{rl}"
    # await client.send_voice(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار ايـه قرآنيه لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["الشيخ","النقشبندي"], ""), group=40986)
# async def ithd(client: Client, message: Message):
    # rl = random.randint(1,90)
    # url = f"https://t.me/ggcnjj/{rl}"
    # await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["فيلم"], ""), group=90098)
# async def ihud(client: Client, message: Message):
    # rl = random.randint(1,50)
    # url = f"https://t.me/gyigkk/{rl}"
    # await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )

# @app.on_message(filters.command(["استوري"], ""), group=1209)
# async def ihgd(client: Client, message: Message):
    # rl = random.randint(1,50)
    # url = f"https://t.me/yoipopl/{rl}"
    # await client.send_audio(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار استوري لك من استار",parse_mode=enums.ParseMode.HTML)
    # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                # ],
            # ]
        # )



###كيب

@app.on_message(filters.command(["غني","غنيلي"], ""), group=765432)
async def ihppd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/gukygn/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥀✨ ¦ تـم اختيـار الاغـنـية لك من استار" ,parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
        


@app.on_message(filters.command(["صوره ", "🕷", "صورهه", "صور"], ""), group=6)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
    
@app.on_message(filters.command(["استوري ", "استوريهات"], ""), group=7876)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["قران ", "قران"], ""), group=34545)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["صور انمي", "انمي"], ""), group=7809)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["اقتباسات ", "اقتباس"], ""), group=8897)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["متحركة ", " متحركه "], ""), group=6009)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["صور بنات"], ""), group=3342)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["صور شباب", " افتار شباب"], ""), group=7654)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار الاغـنـية لـك\n➧ ˹𝙅𝙊𝙄𝙉 |⌯˼ @SOURCE_STARl🐉 ¦",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )        