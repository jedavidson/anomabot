import requests

RANDOM_PROBLEM_URL = 'https://leetcode.com/problems/random-one-question/all'


def get_random_problem() -> str:
    ''' Returns the URL of a random LeetCode problem. '''
    return requests.get(RANDOM_PROBLEM_URL).url
