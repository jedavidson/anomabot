# anomabot.py: Core module for Anomabot
# by James Davidson

import discord
import discord.ext.commands

import modules.utilities as utilities
import modules.nato as nato
import modules.vigenere as vigenere
import modules.unsw as unsw
import modules.leetcode as leetcode
import modules.emojify as emojify

# Create a Discord client instance for the bot, and load its settings
anomabot = discord.ext.commands.Bot(command_prefix='^')
anomabot.bot_settings = utilities.get_bot_data()
settings = anomabot.bot_settings


###########
# General #
###########


@anomabot.event
async def on_ready():
    ''' Performs some initialisation tasks on start up. '''

    print(f'{utilities.get_timestamp()} {anomabot.user} is online!')

    await anomabot.change_presence(activity=discord.Game(name='^help'))


@anomabot.event
async def on_message(msg):
    ''' Delegates messages to the appropriate command/module. '''

    await anomabot.process_commands(msg)


####################
# Command handlers #
####################


@anomabot.command(name='stop', hidden=True)
async def _stop(ctx):
    ''' Stops the bot when ^stop or any other aliases are detected.

        If the user who issues the command is not the 'bot master' (i.e. me),
        a warning is sent to the channel and the bot will remain active.
    '''

    if ctx.message.author.id != settings['bot_master']:
        await ctx.channel.send(settings['warnings']['stop'])
    else:
        await ctx.channel.send('Shutting down, bye for now!')
        utilities.stop_bot()


@anomabot.command(name='nato', help=settings['help_texts']['nato'])
async def _nato(ctx, *args):
    ''' Encodes or decodes a string using the NATO phonetic alphabet.

        If a string is not supplied, the bot sends a warning message
        to the channel the message was sent in.
    '''

    if not args or len(args) < 2:
        await ctx.channel.send(settings['warnings']['nato'])
    elif args[0] == 'encode':
        await ctx.channel.send(nato.encode(' '.join(args[1:])))
    elif args[0] == 'decode':
        await ctx.channel.send(nato.decode(' '.join(args[1:])))


@anomabot.command(name='vigenere', help=settings['help_texts']['vigenere'])
async def _vigenere(ctx, *args):
    ''' Encodes or decodes a text using the Vigenere cipher.

        If a string and encoding method is not supplied, the bot sends a
        warning message to the channel the message was sent in.
    '''

    if not args or len(args) < 3 or args[0] not in 'kpc':
        await ctx.channel.send(settings['warnings']['vigenere'])
    elif args[0] == 'c':
        await ctx.channel.send(':warning: Ciphertext feedback is not currently supported.')
    else:
        await ctx.channel.send(
            vigenere.encipher(args[0], args[1], ' '.join(args[2:])))


@anomabot.command(name='leetcode', help=settings['help_texts']['leetcode'])
async def _leetcode(ctx):
    ''' Gets a link to a random LeetCode problem. '''

    await ctx.channel.send('Fetching a LeetCode problem for you...')
    await ctx.channel.send(leetcode.get_random_problem())


# Command for the Emojify module
@anomabot.command(name='emojify', help=settings['help_texts']['emojify'])
async def _emojify(ctx, *args):
    ''' Turns a message into its emoji equivalent.

        If a string and encoding method is not supplied, the bot sends a
        warning message to the channel the message was sent in.
    '''

    if not args:
        await ctx.channel.send(settings['warnings']['emojify'])
    else:
        await ctx.channel.send(emojify.emojify_msg(''.join(args)))


###########################
# Entry point for the bot #
###########################


if __name__ == '__main__':
    anomabot.run(settings['bot_token'])
