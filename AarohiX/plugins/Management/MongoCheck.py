from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from AarohiX  import app as bot

mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@bot.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please enter your MongoDB URL after the command. Example: /mongochk your_mongodb_url")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("𝗠𝗼𝗻𝗴𝗼𝗗𝗕 𝗶𝘀 𝗹𝗶𝘃𝗲 𝗮𝗻𝗱 𝗿𝗲𝗮𝗱𝘆 𝘁𝗼 𝗴𝗼! 🚀"")
        except Exception as e:
            await message.reply(f"Failed to connect to MongoDB: {e}")
    else:
        await message.reply("𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝗳𝗮𝗶𝗹𝗲𝗱: 𝗜𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗠𝗼𝗻𝗴𝗼𝗗𝗕 𝗨𝗥𝗟 💔")
