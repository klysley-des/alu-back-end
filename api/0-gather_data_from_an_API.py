#!/usr/bin/python3
"""Fetch and display an employee's TODO progress from a REST API."""

import json
import sys
import urllib.request

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id))

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())

    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    done_tasks = [t for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
