#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries to Reddit API """
    version = 'Mozilla/5.0'
    headers = {
        'User-Agent': version
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    resp = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if resp.status_code != 200:
        return None

    dic = resp.json()
    hot_posts = dic['data']['children']
    add_title(hot_list, hot_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
