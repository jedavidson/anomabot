# nato.py: Encode/decode a message in the NATO phonetic alphabet
# by James Davidson

# Required libraries
import re

nato_alph = {
    "a": "Alfa", "b": "Bravo", "c": "Charlie", "d": "Delta",
    "e": "Echo", "f": "Foxtrot", "g": "Golf", "h": "Hotel",
    "i": "India", "j": "Juliet", "k": "Kilo", "l": "Lima",
    "m": "Mike", "n": "November", "o": "Oscar", "p": "Papa",
    "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango",
    "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "Xray",
    "y": "Yankee", "z": "Zulu", "0": "Zero", "1": "One",
    "2": "Two", "3": "Three", "4": "Four", "5": "Five",
    "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", " ": "(space)"
}

# Return a value's key in the above alphabet, if it exists
def fetch_key(v: str) -> str:
    if v not in nato_alph.values():
        return v
    return list(nato_alph.keys())[list(nato_alph.values()).index(v)]


# Return as a string the NATO alphabet encoding of the given message
# Any message characters not in the above alphabet are stripped
def encode(msg: str) -> str:
    encoded_msg = []
    for c in msg:
        if not c.isspace() and not c.isalnum():
            encoded_msg.append(c)
        elif c.isalpha():
            encoded_msg.append(nato_alph[c.lower()])
        else:
            encoded_msg.append(nato_alph[c])

    return ' '.join(encoded_msg)


# Return as a string the translation of a given NATO message
# Any message characters not in the above alphabet are
def decode(msg: str) -> str:
    decoded_msg = []
    for word in msg.split():
        decoded_msg.append(fetch_key(word))

    return ''.join(decoded_msg)


# Process the input directly from the Discord message, and return the
# appropriate response string from either encode() or decode()
# A pre-prepared help string is returned if the leading argument is invalid
def process(msg: str) -> str:
    if msg.startswith("encode"):
        msg = re.sub(r'^encode\s+', '', msg, re.IGNORECASE)
        reply = encode(msg)
    elif msg.startswith("decode"):
        msg = re.sub(r'^decode\s+', '', msg, re.IGNORECASE)
        reply = decode(msg)
    else:
        reply = "Usage: `^nato [encode | decode] [message]`"
    
    return reply       