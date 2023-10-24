#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    response = res.json()
    dict_task = []
    for y in response:
        name = y.get('username')
        userid = y.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()
        task = []
        for x in tasks:
            dct_task = {"username": name,
                        "task": x.get('title'),
                        "completed": x.get('completed')}
            task.append(dct_task)

    full_task = {str(userid): task}
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as fname:
        json.dump(full_task, fname)
