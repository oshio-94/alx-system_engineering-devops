#!/usr/bin/python3
"""Script to make a request from an API using test JSONPlaceholder"""

import json
import requests
import sys
''' Importing the necessary libraries needed for this project'''

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(user)
    res_json = response.json()
    print('Employee {} is done with tasks'.format(res_json.get('name'),end=""))

    to_dolist = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(to_dolist)
    resj = res.json()
    task = []
    for x in resj:
        if x.get('completed') is True:
            task.append(x)

    print('({}/{}):'.format(len(task), len(resj)))
    for y in task:
        print("\t {}".format(y.get("title")))
