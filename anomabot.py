# anomabot.py: Core module for Anomabot
# by James Davidson

import discord
import discord.ext.commands

import modules.utilities as utilities
import modules.nato as nato
import modules.vigenere as vigenere
import modules.unsw as unsw
import modules.leetcode as leetcode

# Create a Discord client instance for the bot, and load its settings
anomabot = discord.ext.commands.Bot(command_prefix='^')
anomabot.bot_settings = utilities.get_bot_data()


# Initialisation tasks for the bot to perform on start up
@anomabot.event
async def on_ready():
    # Write some content to console
    print(f"{utilities.get_timestamp()} {anomabot.user} is online!")

    # Set presence
    await anomabot.change_presence(activity = discord.Game(name="^help"))


# Delegate messages to the appropriate command/module
@anomabot.event
async def on_message(msg):
    if unsw.contains_wam(msg.content.lower()):
        await unsw.add_wam_reactions(msg)
    else:
        await anomabot.process_commands(msg)


# Stop bot with a Discord message - bot creator only
@anomabot.command(name="stop", hidden=True)
async def _stop(ctx):
    if not ctx.message.author.id == anomabot.bot_settings["bot_master"]:
        await ctx.channel.send(anomabot.bot_settings["warnings"]["stop"])
    else:
        await ctx.channel.send("Shutting down, bye for now!")
        utilities.stop_bot()


# Command for the NATO module
@anomabot.command(name="nato", help="Encode/decode NATO alphabet messages")
async def _nato(ctx, *args):
    if not args or len(args) < 2:
        await ctx.channel.send(anomabot.bot_settings["warnings"]["nato"])
    elif args[0] == "encode":
        await ctx.channel.send(nato.encode(' '.join(args[1:])))
    elif args[0] == "decode":
        await ctx.channel.send(nato.decode(' '.join(args[1:])))


# Command for the Vigenere module
@anomabot.command(name="vigenere", help="Encipher with a Vigenere cipher")
async def _vigenere(ctx, *args):
    if not args or len(args) < 3 or args[0] not in "kpc":
        await ctx.channel.send(anomabot.bot_settings["warnings"]["vigenere"])
    elif args[0] == 'c':
        await ctx.channel.send(
            ":warning: Ciphertext feedback is not currently supported.")
    else:
        await ctx.channel.send(
            vigenere.encipher(args[0], args[1], ' '.join(args[2:])))


# Command for the LeetCode module
@anomabot.command(name="leetcode", help="Get a random LeetCode problem")
async def _leetcode(ctx):
    await ctx.channel.send("Fetching a LeetCode problem for you...")
    await ctx.channel.send(leetcode.get_random_problem())


# Run the bot
anomabot.run(anomabot.bot_settings["bot_token"])