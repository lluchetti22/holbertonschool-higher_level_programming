#!/usr/bin/python3
"""Lists all cities of a user-specified state from hbtn_0e_4_usa safely"""
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
    query = (
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC"
    )
    cursor.execute(query, (sys.argv[4],))
    query_rows = cursor.fetchall()
    
    # Extracting the string from the single-element tuple item
    cities = [row[0] for row in query_rows]
    
    # Joining with commas and space, then appending a trailing newline
    print(", ".join(cities))
    
    cursor.close()
    db.close()
