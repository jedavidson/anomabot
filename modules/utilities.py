# utilities.py: Some general purpose bot functions
# by James Davidson

import json
import os
import datetime


"""
Load and return the bot's data object from its JSON file.
"""
def get_bot_data() -> dict:
    try:
        with open('static/anomabot_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error opening bot data file!")
        os._exit(1)


"""
Return a current timestamp string in the form [HH:MM:SS].
"""
def get_timestamp() -> str:
    return f"[{datetime.datetime.now().strftime('%H:%M:%S')}]"