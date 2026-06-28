#!/usr/bin/python3
"""Lists all cities of a user-specified state from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv,
        passwd=sys.argv,
        db=sys.argv
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (sys.argv,)
    )
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
