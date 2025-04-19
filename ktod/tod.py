import click
from database import add_task, get_tasks


@click.command()
@click.argument('task', type=str)
def add(task):
    add_task(task)


@click.command()
def show():
    for t in get_tasks():
        print(t)