#!/usr/bin/python3
"""
This module starts a
Flask web application with the following specifications:
"""

import requests
import json
import sys

def get_employee_todo_progress(employee_id):
    """display the API information"""
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_data = requests.get(url).json()
    tasks = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}').json()
    tasks_dict = {employee_id: []}
    for task in tasks:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        }
        tasks_dict[employee_id].append(task_data)

    with open(f'{employee_id}.json', 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_employee_todo_progress(sys.argv[1])
