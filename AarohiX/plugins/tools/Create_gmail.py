from pyrogram import filters
import requests
from AarohiX import app
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import json

# New API URL
API_URL = "https://last-warning.serv00.net/Create_Gmail.php"

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_data"),
        InlineKeyboardButton("ᴠᴘʟᴀʏ", callback_data="play"),
    ]
])

@app.on_callback_query(filters.regex("^play"))
async def play_callback(_, query):
    # You can add more logic here before initiating playback
    await query.answer("Playback started!")

@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()

@app.on_message(filters.command("create"))
async def create_gmail(client, message):
    if len(message.command) == 1:
        await message.reply("❖ Please provide your Gmail creation details.")
        return

    # Collect user input from the message
    user_input = ' '.join(message.command[1:])
    
    # Make API call to the Gmail creation endpoint
    try:
        response = requests.post(API_URL, data={"input": user_input})
        response_data = response.json()  # Assuming the response is in JSON format
        if response_data.get('success'):
            await message.reply(f"❖ Gmail account created successfully. Details: {response_data['details']}")
        else:
            await message.reply("❖ Failed to create Gmail account. Please try again.")
    except Exception as e:
        await message.reply(f"❖ Error: {str(e)}")
