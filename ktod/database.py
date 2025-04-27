import click
import pathlib
import os.path as p
from config import __db_path__
from collections import namedtuple
import sqlite3


# Data Models
Task = namedtuple('Task', ['task_name', 'status'])  # Id and timestamp are autoincremented



def setup_db():
    with sqlite3.connect(__db_path__) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS TODAY (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT NOT NULL,
                date DATE DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS PENDING (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT NOT NULL,
                date DATE NOT NULL
            );
        """)

def update_db():
    ...

def add_tasks(*tasks):
    with sqlite3.connect(__db_path__) as conn:
        conn.executemany(f'''
            INSERT INTO TODAY (name, status)
            VALUES (?, ?)
        ''', tasks)


def get_today():
    with sqlite3.connect(__db_path__) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM TODAY;
        ''')
        return cursor.fetchall()
    

def close_tasks(id):
    with sqlite3.connect(__db_path__) as conn:
        conn.execute(f'''
            UPDATE TODAY
            SET status = 'closed'
            WHERE id = {id}
        ''')


if __name__ == '__main__':
    setup_db()
