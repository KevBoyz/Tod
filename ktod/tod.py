import click
from collections import namedtuple
from datetime import date
from database import add_tasks, get_today, Task
from rich import print


@click.command(help='Add a new task for today')
@click.argument('task_name', type=str)
def add(task_name):
    add_tasks(Task(task_name, 'open'))


@click.command(help='See your tasks for today')
def show():
    for t in get_today():
        print(t)