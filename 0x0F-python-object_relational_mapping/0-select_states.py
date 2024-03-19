#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


def list_states(username, password, database):
    """
    Connects to the MySQL database and lists all states.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", user=username, port=3306,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
    else:
        username, password, database = argv[1:]
        list_states(username, password, database)
