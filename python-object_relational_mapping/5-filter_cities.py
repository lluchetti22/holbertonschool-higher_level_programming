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
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    query_rows = cursor.fetchall()
    
    # Safely extract the string from index 0 of every single row tuple
    cities = [row[0] for row in query_rows]
    
    # Print the comma-separated string exactly as required
    print(", ".join(cities))
    
    cursor.close()
    db.close()
