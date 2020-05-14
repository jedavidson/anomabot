# nato.py: Encode/decode a message in the NATO phonetic alphabet
# by James Davidson

import re

NATO_ALPH = {
    'a': 'Alfa', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta',
    'e': 'Echo', 'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel',
    'i': 'India', 'j': 'Juliet', 'k': 'Kilo', 'l': 'Lima',
    'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa',
    'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
    'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'Xray',
    'y': 'Yankee', 'z': 'Zulu', '0': 'Zero', '1': 'One',
    '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
    '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', ' ': '(space)'
}


####################
# Helper functions #
####################


def _fetch_key(val: str) -> str:
    ''' Returns a value's key in the above alphabet, if it exists. '''

    if val not in NATO_ALPH.values():
        return val

    return list(NATO_ALPH.keys())[list(NATO_ALPH.values()).index(val)]


######################
# Main functionality #
######################


def encode(msg: str) -> str:
    ''' Returns as a string the NATO alphabet encoding of the given message.
        Any message characters not in the above alphabet are stripped.
    '''

    encoded_msg = []

    for ch in msg:
        if not ch.isspace() and not ch.isalnum():
            encoded_msg.append(ch)
        else:
            encoded_msg.append(NATO_ALPH[ch.lower()])

    return ' '.join(encoded_msg)


def decode(msg: str) -> str:
    ''' Returns as a string the translation of a given NATO message.
        Any message characters not in the above alphabet are stripped.
    '''

    decoded_msg = []

    for word in msg.split():
        decoded_msg.append(_fetch_key(word))

    return ''.join(decoded_msg)
