# vigenere.py: Encipher a message with a Vigenere cipher
# by James Davidson

import re


####################
# Helper functions #
####################


def _encipher_char(ch: str, cipher_key: str) -> str:
    ''' Returns the shifted character according to the cipher key.
        The case of the original character is preserved.
    '''

    shifted_ch = ord(ch.lower()) + ord(cipher_key.lower()) - ord('a')

    if shifted_ch > ord('z'):
        shifted_ch -= 26

    return chr(shifted_ch).upper()


######################
# Main functionality #
######################


def encipher(method: str, keyword: str, plaintext: str) -> str:
    ''' Returns as a string the enciphered text using a given keyword.
        Punctuation, spaces and non-alphabetic characters are left as is,
        but non-alphabetic characters in the keyword are stripped.

        The method parameter dictates how any remaining space in the key after
        the keyword is filled to match the length of the plaintext:
        - 'k' recycles the given keyword
        - 'p' feeds the plaintext into the remaining space
        - 'c' feeds the ciphertext into the remaining space
    '''

    keyword = re.sub(r'[^a-zA-Z]', '', keyword)
    no_punct = re.sub(r'[^a-zA-Z]', '', plaintext)

    alpha_count = 0
    ciphertext = ''

    for ch in plaintext:
        if ch.isalpha():
            cipher_key = ''
            if method == 'k' or alpha_count < len(keyword):
                cipher_key = keyword[alpha_count % len(keyword)]
            elif method == 'p':
                cipher_key = no_punct[alpha_count - len(keyword)]
            # TODO: fix ciphertext feedback
            # elif method == 'c':
            # 	...

            ciphertext += _encipher_char(ch, cipher_key)
            alpha_count += 1
        else:
            ciphertext += ch

    return ciphertext
