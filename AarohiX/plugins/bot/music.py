from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app
from config import BOT_USERNAME
#from AarohiX.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ 𝗧ɢ 𝗡ᴀᴍᴇ - [⏤꯭𓆰𝅃꯭꯭꯭꯭꯭꯭꯭꯭꯭꯭꯭᳚⋏ ꯭y꯭ ᴜ꯭ s ꯭ʜ |꯭ ˹𐩃꯭ᴅ꯭˼ ꯭[꯭🇮🇳꯭]](https://t.me/MOH_MAYA_OFFICIAL)
│├ 𝗙ᴜʟʟ 𝗜ɴғᴏ - [𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ](https://t.me/MOH_MAYA_OFFICIAL)
│├─────────────────╯
├┼─────────────────⦿
│├─────────────────╮
│├ 𝗢ᴡɴᴇʀ│ [⏤꯭𓆰𝅃꯭꯭꯭꯭꯭꯭꯭꯭꯭꯭꯭᳚⋏ ꯭y꯭ ᴜ꯭ s ꯭ʜ |꯭ ˹𐩃꯭ᴅ꯭˼ ꯭[꯭🇮🇳꯭]](https://t.me/MOH_MAYA_OFFICIAL)
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("\x41\x4C\x4F\x4E\x45\x20\x43\x4F\x44\x45\x52", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x68\x75\x56\x61\x69")
        ],
        [
          InlineKeyboardButton("\x41\x4C\x4C\x20\x52\x45\x50\x4F", url="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x55\x70\x64\x61\x74\x65\x73\x2F\x31\x30\x37"),
          InlineKeyboardButton("\x52\x45\x50\x4F", url="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x54\x65\x61\x6D\x41\x6C\x6F\x6E\x65\x4F\x70\x2F\x41\x6C\x6F\x6E\x65\x58"),
          ],
               [
                InlineKeyboardButton("\x41\x4C\x4F\x4E\x45\x20\x4E\x45\x54\x57\x4F\x52\x4B", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x55\x70\x64\x61\x74\x65\x73"),
],
[
InlineKeyboardButton("\x4F\x46\x46\x49\x43\x49\x41\x4C\x20\x42\x4F\x54", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x58\x4D\x75\x73\x69\x63\x42\x6F\x74"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo=https://graph.org/file/bba38ef4b40c6860f52f5-72adfc3f156cb27ee7.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )