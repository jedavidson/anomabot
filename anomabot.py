# anomabot.py: Core module for Anomabot
# by James Davidson

# Required libraries and modules
import discord

import modules.utilities as utilities
import modules.nato as nato
import modules.anagram as anagram
import modules.unsw as unsw


anomabot = discord.Client()


# Initialisation tasks for the bot to perform on start up
@anomabot.event
async def on_ready():
    # Write some content to console
    print(f"{anomabot.user} is now online!")
    print(f"-> Launch time: {utilities.get_timestamp()}")

    # Set presence
    await anomabot.change_presence(activity = discord.Game(name = "^help"))


# Delegate message types to the appropriate module
@anomabot.event
async def on_message(msg):
    # Ignore messages from the bot itself
    if msg.author == anomabot.user:
        return

    # Strip the prefix and command name only
    # Processing arguments is handled by each module separately
    args = utilities.trim_msg(msg.content)

    # NATO encoding/decoding
    if msg.content.startswith("^nato"):
        reply = nato.process(args)
        await msg.channel.send(reply)


# Prime the bot for start up
anomabot.bot_settings = utilities.get_bot_data()
anomabot.run(anomabot.bot_settings['bot_token'])