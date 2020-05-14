# leetcode.py: Get a random LeetCode problem
# by James Davidson

import requests

RANDOM_PROBLEM_URL = 'https://leetcode.com/problems/random-one-question/all'


"""
Return the URL of a random LeetCode problem.
"""
def get_random_problem() -> str:
    return requests.get(RANDOM_PROBLEM_URL).url
