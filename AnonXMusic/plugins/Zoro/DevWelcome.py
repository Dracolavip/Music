from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
import os
from AnonXMusic import app
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

@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 6586941458
    if response.from_user.id == dev_id and response.new_chat_member.status == ChatMemberStatus.MEMBER:
        info = await app.get_chat(dev_id)
        name = info.first_name
        username = info.username
        bio = info.bio
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(name, url=f"{username}.t.me")
             ],[
                    InlineKeyboardButton(
                        "ＳＯＵＲＣＥ ＤＲＡＣＵＬＡ", url=f"https://t.me/D_A_003"),
                ],
        ])
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f" نورتني » {name}\n صاحب سورس"
        )
        
        
        