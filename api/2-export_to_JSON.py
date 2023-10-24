#!/usr/bin/python3

"""
Export Employee TODO Progress to JSON

This script fetches an employee's TODO list and creates a JSON file with the data.
The script takes an employee ID as a command-line argument and generates a JSON
file containing the employee's TODO tasks in the desired format.

Usage:
    python script_name.py employee_id

Args:
    employee_id (int): The ID of the employee for whom to fetch the TODO list
        and create a JSON file.

Example:
    To export the TODO progress of an employee with ID 2:
    python script_name.py 2
"""



"""
Python script to export data to a JSON file.
"""

import json
import requests
import sys


def export_to_CSV(user_id):
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()["username"]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    ).json()

    tasks_data = {str(user_id): []}

    for task in tasks:
        tasks_data[str(user_id)].append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name,
            }
        )

    with open(str(user_id) + ".json", "w", encoding="UTF8", newline="") as f:
        json.dump(tasks_data, f)


if __name__ == "__main__":
    export_to_CSV(sys.argv[1])