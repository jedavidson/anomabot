# vigenere.py: Encipher a message with a Vigenère cipher
# by James Davidson


import re


# Return as a string the enciphered text using a given keyword.
# Punctuation, spaces and non-alphabetic characters are left as is,
# but non-alphabetic characters in the keyword are stripped.
#
# The method parameter dictates how any remaining space in the key after
# the keyword is filled to match the length of the plaintext:
# -> "k" recycles the given keyword
# -> "p" feeds the plaintext into the remaining space
# -> "c" feeds the ciphertext into the remaining space
#
# Parameters:
# -> text:    the text to encipher
# -> method:  the method to use for key feedback
# -> keyword: initial part of the cipher key to get Caesar ciphers
def encipher(text: str, method: str, keyword: str) -> str:
    # TODO.
    return "abc"

# Process the input directly from the Discord message, and return the
# appropriate response string from encode().
# A pre-prepared help string is returned if the leading argument is invalid.
# Parameters:
# -> msg: raw content of the Discord message, with prefix/command trimmed
def process(msg: str) -> str:
    args = msg.split()
    if len(args) < 3 or not re.match(r'^[spc]$', args[0], re.IGNORECASE):
        reply = "Usage: `^vigenere [method] [keyword] [message]`"
    else:
        method = args[0]
        keyword = re.sub(r'[^a-z]', '', args[1])
        text = ' '.join(args[2:])
        reply = encipher(text, method, keyword)
    return reply