#!/usr/bin/python3
"""
This module starts a
Flask web application with the following specifications:
"""

import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    """display the API information"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from API.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    tasks = [task for task in todos_data] 
    total_tasks = len(todos_data)
    nameFILE = str(employee_id) + ".csv"
    with open(nameFILE, 'w') as f:
        writer = csv.writer(f)
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, user_data['name'], task['completed'], task['title']])
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument.")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as the employee ID.")
