#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

def filter_states(username, password, database):
    """
    Connects to the database and retrieves states starting with 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.

    Returns:
        None
    """
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", user=username, port=3306,
                             passwd=password, db=database)

        # Create a cursor object
        cur = db.cursor()

        # Execute the SQL query
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

        # Fetch all the rows
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error accessing MySQL database: {e}")
    finally:
        # Close the cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == '__main__':
    # Check if the correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
    else:
        # Extract command-line arguments
        username, password, database = argv[1], argv[2], argv[3]
        
        # Call the filter_states function
        filter_states(username, password, database)

