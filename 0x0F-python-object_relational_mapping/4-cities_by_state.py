#!/usr/bin/python3
"""Lists states"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
