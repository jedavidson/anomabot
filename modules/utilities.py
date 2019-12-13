# utilities.py: Some general purpose bot functions
# by James Davidson

# Required libraries
import json
import sys
import re
import datetime


# Load and return the bot's data object from its JSON file
def get_bot_data() -> dict:
    try:
        with open('static/anomabot_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error opening bot data file!")
        sys.exit(1)


# Return a message string with the prefix and command name trimmed
# Extraneous spaces between the command name and arguments is stripped
def trim_msg(msg: str) -> str:
    return re.sub(r'^\^[a-z0-9]+\s+', '', msg, flags=re.IGNORECASE)

# Return a current timestamp string in the form HH:MM:SS
def get_timestamp() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')