#!/usr/bin/python3
"""
This module starts a Flask web application with the following specifications.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Display the API information."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_data = requests.get(user_url).json()
    tasks = requests.get(todos_url).json()

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, user_data['username'],
                             str(task['completed']), task['title']])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        get_employee_todo_progress(sys.argv[1])
