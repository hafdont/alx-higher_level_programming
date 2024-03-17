#!/usr/bin/python3
"""
This script lists all states with
a 'name' starting with the letter 'N'
from the database 'hbtn_0e_0_usa'.
"""
import MySQLdb
import sys

def filter_states(username, password, database):
    """
    List all states with a name string with "N" from the given database

    Args:
        username (str): MySQLdb username
        password (str): MySQL password
        database (str): Name of database.

    Returns:
        None
    """

    db = mySQLdb.connect(host="localhost",
            port=3306.
            user=username,
            passwd=password,
            db=database)
    cursor = db.cursor()
    cursor execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    filter_states(username, password, database)
