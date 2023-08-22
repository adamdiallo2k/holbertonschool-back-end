#!/usr/bin/python3
"""
This module starts a
Flask web application with the following specifications:
"""


import json
import requests


def main():
    """display the API information"""

    # Fetch all users
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    lenUser = len(users)
    tasks_dict = {}

    for i in range(1, lenUser + 1):
        url = f'https://jsonplaceholder.typicode.com/users/{i}'
        user_data = requests.get(url).json()
        tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={i}').json()

        tasks_dict[i] = []
        for task in tasks:
            task_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            }
            tasks_dict[i].append(task_data)

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)

if __name__ == '__main__':
    main()


