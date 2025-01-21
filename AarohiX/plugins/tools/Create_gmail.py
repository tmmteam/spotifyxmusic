from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests

# Initialize the Pyrogram Client (AarohiX bot)
app = Client("AarohiX")

# Constants for the new URLs
ad_image_url = 'https://iili.io/24UDx6b.md.jpg'
create_gmail_url = "https://last-warning.serv00.net/Create_Gmail.php"
inbox_url = "https://last-warning.serv00.net/Inbox.php"

# Store emails for users
user_emails = {}

# Inline keyboard
keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Create Gmail", callback_data="create_gmail"),
        InlineKeyboardButton("Inbox 📥", callback_data="inbox")
    ]
])

@app.on_message(filters.command("starts"))
async def send_welcome(client, message):
    # Send welcome message with ad image and buttons
    await message.reply_photo(
        ad_image_url, 
        caption="Welcome to the Last Warning Bot!", 
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("^create_gmail"))
async def create_gmail(_, query):
    # Simulate Gmail creation (replace with actual request to create Gmail)
    payload_create_gmail = {
        'parameter1': 'value1',  # Replace with real parameters
        'parameter2': 'value2',  # Replace with real parameters
    }
    
    response = requests.post(create_gmail_url, data=payload_create_gmail)
    
    if response.status_code == 200:
        # Assuming response contains the generated email
        response_data = response.json()
        email = response_data.get("email")
        
        if email:
            # Store email and send response
            user_emails[query.message.chat.id] = email
            await query.answer(f"Generated Email: {email}")
            await query.message.reply("You can now check your inbox using the 'Inbox 📥' button.")
        else:
            await query.message.reply("Failed to generate email.")
    else:
        await query.message.reply(f"Error creating Gmail. Status code: {response.status_code}")

@app.on_callback_query(filters.regex("^inbox"))
async def check_inbox(_, query):
    # Check if the user has a generated email
    if query.message.chat.id not in user_emails:
        await query.message.reply("Please generate a Gmail account first using the 'Create Gmail' button.")
        return

    email = user_emails[query.message.chat.id]

    # Request inbox details
    inbox_request_url = f"{inbox_url}?raj={email}"
    response_inbox = requests.get(inbox_request_url)
    
    if response_inbox.status_code == 200:
        # Process inbox data (assuming it contains a 'subject')
        inbox_data = response_inbox.json()
        subject = inbox_data.get("subject", "No subject found.")
        await query.message.reply(f"Inbox Message: {subject}")
    else:
        await query.message.reply(f"Error checking inbox. Status code: {response_inbox.status_code}")

# Start the bot
app.run()
