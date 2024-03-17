#!/usr/bin/python3
"""
This script lists all states from the tabase  `hbtn_0e_0_usa`
"""


import MySQLdb
import sys import argv

if __name__ == "__main__":
    """
    Get the args, assign them to usr, pwd, and db,
    create a cursor, execute a query.
    show the resutls. then close the cursor and db.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(states)

    cursor.close()
    db.close()
