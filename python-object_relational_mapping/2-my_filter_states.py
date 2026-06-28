#!/usr/bin/python3
"""Displays all values in the states table matching the user input argument"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            sys.argv[4]
        )
    )
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
