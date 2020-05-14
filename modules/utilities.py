# utilities.py: Some general purpose bot functions
# by James Davidson

import json
import os
import datetime


######################
# Main functionality #
######################


def get_bot_data() -> dict:
    ''' Loads and returns the bot's data object from its JSON file. '''

    try:
        with open('static/anomabot_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error opening bot data file!")
        os._exit(1)


def get_timestamp() -> str:
    ''' Returns a current timestamp string in the form [HH:MM:SS]. '''

    return f"[{datetime.datetime.now().strftime('%H:%M:%S')}]"


def stop_bot():
    ''' Stops the bot script, shutting down the bot. '''

    os._exit(1)
