# leetcode.py: Get a random LeetCode problem
# by James Davidson

import requests

random_problem_url = 'https://leetcode.com/problems/random-one-question/all'


"""
Return the URL of a random LeetCode problem.
"""
def get_random_problem():
    problem_url = requests.get(random_problem_url).url
    return problem_url