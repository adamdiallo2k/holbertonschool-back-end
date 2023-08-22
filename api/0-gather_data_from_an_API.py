#!/usr/bin/python3
"""
This module starts a
Flask web application with the following specifications:
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """display the API information"""
    user_url = f"https://jsonplaceholder.typicode.com/
    users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/
    users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from API.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed_tasks = [task for task in todos_data 
    if task['completed']]
    total_tasks = len(todos_data)

    print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as the employee ID.")
