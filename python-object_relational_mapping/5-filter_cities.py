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
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (sys.argv,)
    )
    query_rows = cursor.fetchall()
    
    # Correctly grab the full string element from each database tuple
    cities = [row[0] for row in query_rows]
    
    # Print as a comma-separated string
    print(", ".join(cities))
    
    cursor.close()
    db.close()
