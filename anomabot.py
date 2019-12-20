# anomabot.py: Core module for Anomabot
# by James Davidson

import discord
import discord.ext.commands

import modules.utilities as utilities
import modules.nato as nato
import modules.vigenere as vigenere
import modules.unsw as unsw

# Create a Discord client instance for the bot
anomabot = discord.ext.commands.Bot(command_prefix='^')


# Initialisation tasks for the bot to perform on start up
@anomabot.event
async def on_ready():
    # Write some content to console
    print(f"{utilities.get_timestamp()} {anomabot.user} is online!")

    # Set presence
    await anomabot.change_presence(activity = discord.Game(name = "^help"))


# Delegate messages to the appropriate command/module
@anomabot.event
async def on_message(msg):
    await anomabot.process_commands(msg)


# Stop bot with a Discord message - bot creator only
@anomabot.command(name="stop", hidden=True)
async def _stop(ctx):
    if not ctx.message.author.id == anomabot.bot_settings["bot_master"]:
        await ctx.channel.send(":no_entry: You're not my master!")
    else:
        await ctx.channel.send("Shutting down, bye for now!")
        utilities.stop_bot()
    

# Command for the NATO module
@anomabot.command(name="nato", help="Encode/decode NATO alphabet messages")
async def _nato(ctx, *args):
    if not args or len(args) < 2:
        await ctx.channel.send(
            ":warning: Usage: `^nato [encode | decode] [message]`"
        )
    elif args[0] == "encode":
        await ctx.channel.send(nato.encode(' '.join(args[1:])))
    elif args[0] == "decode":
        await ctx.channel.send(nato.decode(' '.join(args[1:])))


# Command for the Vigenere module
@anomabot.command(name="vigenere", help="Encipher with a Vigenere cipher")
async def _vigenere(ctx, *args):
    await ctx.channel.send(":no_entry: This command is not ready yet!")


# Prime the bot for start up
anomabot.bot_settings = utilities.get_bot_data()
anomabot.run(anomabot.bot_settings["bot_token"])