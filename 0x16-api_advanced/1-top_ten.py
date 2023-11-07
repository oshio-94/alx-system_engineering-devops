#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """ Queries to Reddit API """
    version = 'Mozilla/5.0'
    headers = {
        'User-Agent': version
    }
    params = {
        'limit': 10
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    resp = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if resp.status_code != 200:
        print(None)
        return
    diction = resp.json()
    posts = diction['data']['children']
    if len(posts) is 0:
        print(None)
    else:
        for post in posts:
            print(post['data']['title'])
