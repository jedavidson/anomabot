# unsw.py: Functionality related to UNSW and the UNSW Discord server
# by James Davidson

import re


"""
Determine if a message contains the word "wam" (case insensitive).
"""
def contains_wam(msg: str) -> bool:
    return bool(re.search(r'\bwam\b', msg, re.IGNORECASE))


"""
Add a series of WAM emoji reactions whenever a message is sent that
contains "wam" (case insensitive) as its own word.
"""
async def add_wam_reactions(msg: object):
	for react in ['🇼', '🇦', '🇲']:
		await msg.add_reaction(react)