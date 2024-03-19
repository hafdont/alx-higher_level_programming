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
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=username, port=3306,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states")

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
    else:
        # Extract command line arguments
        username, password, database = argv[1:]

        # Call the function to list states
        list_states(username, password, database)
