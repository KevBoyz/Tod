import click
import pathlib
from config import __version__
from database import setup_db 

from tod import *


setup_db()


@click.group('global')
@click.version_option(__version__)
def Global():
    """Tod 0.1.0 by Kevboyz"""
    

Global.add_command(add)
Global.add_command(show)



Global()
