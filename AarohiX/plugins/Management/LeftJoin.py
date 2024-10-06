from AarohiX import app as bot
from pyrogram import filters
from pyrogram.errors import RPCError, ChatAdminRequired
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

@bot.on_chat_member_updated(filters.group, group=10)
async def member_has_joined(client: bot, member: ChatMemberUpdated):
    if (
        member.new_chat_member
        and member.new_chat_member.status not in {"banned", "left", "restricted"}
        and not member.old_chat_member
    ):
        pass
    else:
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        if user.is_bot:
            return
    except ChatAdminRequired:
        return

    
    try:
        username = user.username
        url = f"https://t.me/{username}" if username else f"tg://openmessage?user_id={user.id}"

        user_button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    f"⦿ ɪɴғᴏ ⦿",
                    url=url
                )
            ]
        ])

        caption = (
            f"😢 ɢᴏᴏᴅʙʏᴇ {user.mention}!** 😔\n\n"
            f"🌈 ᴡᴇ'ʟʟ ᴍɪss ʏᴏᴜ! ɪᴅ ʏᴏᴜ ᴇᴠᴇʀ ᴅᴇᴄɪᴅᴇ ᴛᴏ ʀᴇᴛᴜʀɴ, ᴏᴜʀ ᴅᴏᴏʀs ᴀʀᴇ ᴀʟᴡᴀʏs ᴏᴘᴇɴ.\n\n"
            f"📅 ʟᴇғᴛ ᴅᴀᴛᴇ : {get_formatted_datetime()}"
        )

        await client.send_animation(
            chat_id=member.chat.id,
            animation="https://envs.sh/BA8.mp4",
            caption=caption,
            reply_markup=user_button,
        )
        return
    except RPCError as e:
        print(e)
        return

def get_formatted_datetime():
    now = datetime.utcnow()
    formatted_datetime = now.strftime("%A, %B %d, %Y %H:%M:%S UTC")
    return formatted_datetime
