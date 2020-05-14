# emojify.py: Convert a message into its letter emoji equivalent
# by James Davidson

SPELLING = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}


def emojify_msg(msg: str) -> str:
    ''' Returns as a string the emojified version of a given message. '''

    emojified_msg = ''
    
    for ch in msg:
        if ch.isalpha():
            emojified_msg += f':regional_indicator_{ch.lower()}:'
        elif ch.isdigit():
            emojified_msg += f':{SPELLING[ch]}:'
        else:
            emojified_msg += ch

    return emojified_msg
