# vigenere.py: Encipher a message with a Vigenère cipher
# by James Davidson


import re


"""
Return as a string the enciphered text using a given keyword.
Punctuation, spaces and non-alphabetic characters are left as is,
but non-alphabetic characters in the keyword are stripped.

The method parameter dictates how any remaining space in the key after
the keyword is filled to match the length of the plaintext:
- "k" recycles the given keyword
- "p" feeds the plaintext into the remaining space
- "c" feeds the ciphertext into the remaining space

Parameters:
- text:    the text to encipher
- method:  the method to use for key feedback
- keyword: initial part of the cipher key to produce the cipher
"""
def encipher(text: str, method: str, keyword: str) -> str:
    return "Under construction!"