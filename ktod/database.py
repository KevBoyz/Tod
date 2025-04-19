import click
import json
import pathlib
import os.path as p
from config import __db_path__


def setup_db():
    """
    If a database does't exist, create one in package root.
    """
    if not p.exists(__db_path__):
        db_dict = {
            'tasks': []
        }
        with open(__db_path__, 'w') as file:
            file.write(json.dumps(db_dict))


def add_task(task: str) -> None:
    with open(__db_path__, 'r') as file:
        content = json.loads(file.read())
    content['tasks'].append(task)
    with open(__db_path__, 'w') as file:
        file.write(json.dumps(content))


def get_tasks()-> list: 
    with open(__db_path__, 'r') as file:
        content = json.loads(file.read())
    return content['tasks']
