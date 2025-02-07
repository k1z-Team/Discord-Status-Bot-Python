import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the bot token from the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Set activity settings here:
ACTIVITY_TYPE = discord.ActivityType.playing  # Options: playing, watching, listening, streaming
ACTIVITY_TEXT = "K1z Cash Economy"  # Custom text for the status
STREAM_URL = "https://twitch.tv/example"  # Only needed if ACTIVITY_TYPE is "streaming"

# Create the bot instance
client = discord.Client()

# Event listener for when the bot is ready
@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

    # Set the bot's activity
    if ACTIVITY_TYPE == discord.ActivityType.streaming:
        activity = discord.Activity(type=ACTIVITY_TYPE, name=ACTIVITY_TEXT, url=STREAM_URL)
    else:
        activity = discord.Activity(type=ACTIVITY_TYPE, name=ACTIVITY_TEXT)

    await client.change_presence(activity=activity)
    print(f"✅ Status set to: {ACTIVITY_TYPE} {ACTIVITY_TEXT}")

# Run the bot using the bot token from .env
client.run(BOT_TOKEN)
