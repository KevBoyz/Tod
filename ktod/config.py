import configparser
import pathlib
import os.path as p


# Enviroment variables
__version__ = '0.1.0'

__package_root__ = pathlib.Path(__file__).resolve().parent
__db_path__ = p.join(__package_root__, 'database.db')


