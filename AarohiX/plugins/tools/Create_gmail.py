from pyrogram import filters
import requests
from AarohiX import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# API URLs
CREATE_API_URL = "https://last-warning.serv00.net/Create_Gmail.php"
INBOX_API_URL = "https://last-warning.serv00.net/Inbox.php?raj={email}"

# Command: /start
@app.on_message(filters.command("starts"))
async def start_command(_, message):
    await message.reply(
        "Welcome to Last Warning Temp Mail 💌 Bot!\n\n"
        "Use the following commands:\n"
        "- `/help` to see all available commands.\n"
        "- `/create` to generate a temporary email.\n"
        "- `/inbox` to check your email inbox.\n"
        "- `/old_inbox` to re-check a specific email inbox."
    )

# Command: /help
@app.on_message(filters.command("helps"))
async def help_command(_, message):
    await message.reply(
        "**Help Menu:**\n\n"
        "Here are the available commands:\n"
        "- `/start`: Welcome message and basic instructions.\n"
        "- `/help`: View this help menu.\n"
        "- `/create`: Generate a new temporary email.\n"
        "- `/inbox`: Check the inbox of your generated email.\n"
        "- `/old_inbox`: Check the inbox for a manually entered email.\n"
    )

# Command: /create
@app.on_message(filters.command("create"))
async def create_command(_, message):
    try:
        # Call the API to generate a new email
        response = requests.post(CREATE_API_URL)
        response_data = response.json()

        if response_data.get("email"):
            email = response_data["email"]
            await message.reply(f"Here is your Gmail provided by Last Warning:\n\n**Email:** `{email}`")
            
            # Store the email in the user-specific context
            await app.set_user_data(message.chat.id, {"temp_email": email})
        else:
            await message.reply("❖ Failed to create Gmail account. Please try again.")
    except Exception as e:
        await message.reply(f"❖ Error: {str(e)}")

# Command: /inbox
@app.on_message(filters.command("inbox"))
async def inbox_command(_, message):
    # Retrieve the email from the user's stored data
    user_data = await app.get_user_data(message.chat.id)
    email = user_data.get("temp_email")

    if not email:
        await message.reply("❖ No email found. Please create an email first using `/create`.")
        return

    try:
        # Call the API to fetch the inbox for the stored email
        response = requests.get(INBOX_API_URL.format(email=email))
        response_data = response.json()

        if response_data.get("messages"):
            messages = "\n\n".join(response_data["messages"])
            await message.reply(f"Here are your inbox messages:\n\n{messages}")
        else:
            await message.reply("Your inbox is empty.")
    except Exception as e:
        await message.reply(f"❖ Error: {str(e)}")

# Command: /old_inbox
@app.on_message(filters.command("old_inbox"))
async def old_inbox_command(_, message):
    await message.reply("❖ Please enter your Gmail address.")

    @app.on_message(filters.reply)
    async def fetch_old_inbox(_, reply_message):
        email = reply_message.text

        try:
            # Call the API to fetch the inbox for the provided email
            response = requests.get(INBOX_API_URL.format(email=email))
            response_data = response.json()

            if response_data.get("messages"):
                messages = "\n\n".join(response_data["messages"])
                await reply_message.reply(f"Here are your old inbox messages for `{email}`:\n\n{messages}")
            else:
                await reply_message.reply(f"The inbox for `{email}` is empty.")
        except Exception as e:
            await reply_message.reply(f"❖ Error: {str(e)}")
