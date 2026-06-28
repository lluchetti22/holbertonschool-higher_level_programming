#!/usr/bin/python3
"""Lists all cities of a user-specified state from hbtn_0e_4_usa safely"""
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
    query = (
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC"
    )
    cursor.execute(query, (sys.argv,))
    query_rows = cursor.fetchall()
    
    # Correctly isolate the first index element from the database tuples
    cities = [row for row in query_rows]
    
    print(", ".join(cities))
    
    cursor.close()
    db.close()
