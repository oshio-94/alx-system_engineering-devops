#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    version = 'Mozilla/5.0'
    headers = {
        'User-Agent': version
    }
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return 0
    dic = resp.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return resp.json()['data']['subscribers']
