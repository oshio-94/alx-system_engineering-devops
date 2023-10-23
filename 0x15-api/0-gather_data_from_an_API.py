#!/usr/bin/python3
#Script to make a request from an API

import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'
users = '{}users/{}'.format(url, sys.argv[1])
response = requests.get(users)
res_json = response.json()
print('Employee {} is done with tasks'.format(res_json.get('name'),end=' '))

to_dolist = '{}todos?userId={}'.format(url, sys.argv[1])
res = requests.get(to_dolist)
resj = res.json()
task = []
for x in resj:
    if x.get('completed') is True:
      task.append(x)

print('{}/{}'.format(len(task), len(resj)))
for y in task:
 print("\n {}".format(y.get("title")))
