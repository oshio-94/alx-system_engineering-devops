#!/usr/bin/python3
"""Script to make a request from an API using test JSONPlaceholder"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(user)
    res_jsn = response.json()
    usrname = res_jsn.get('username')

    to_dolist = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(to_dolist)
    resj = res.json()
    task = []
    for x in resj:
        task.append([sys.argv[1], usrname, x.get('completed'), x.get('title')])

    filename = '{}.csv'.format(sys.argv[1])
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile,
                               delimiter=',',
                               quoting=csv.QUOTE_ALL)
        for x in task:
            csvwriter.writerow(x)
