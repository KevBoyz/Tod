import click
from collections import namedtuple
from datetime import date
from database import  *

from rich import print
from rich.table import Table


@click.command(help='Add a new task for today')
@click.argument('task_name', type=str)
def add(task_name):
    add_tasks(Task(task_name, 'open'))


@click.command(help='See your tasks for today')
def show():

    table = Table()
    table.add_column('id', style='cyan')
    table.add_column('name', style='gold1')
    table.add_column('status')
    table.add_column('date', style='magenta')

    for t in get_today():
        if t[2] == 'open':
            table.add_row(str(t[0]), t[1], f'[green]{t[2]}', t[3])
        else:
            table.add_row(str(t[0]), t[1], f'[red]{t[2]}', t[3])
    print(table)

@click.command(help='Close your tasks')
@click.argument('id', type=int)
def done(id):
    close_tasks(id)
