#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (argv[4],))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()

