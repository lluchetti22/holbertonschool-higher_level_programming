#!/usr/bin/python3
"""
Lists all cities of a user-specified state from the database hbtn_0e_4_usa.
Safe from MySQL injection.
"""
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
    
    # Selecting purely cities.name matching the input parameter
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    
    query_rows = cursor.fetchall()
    
    # Using a clean list comprehension with structural index extraction
    cities = [row[0] for row in query_rows]
    
    # This guarantees a blank line is printed even if the cities list is empty
    print(", ".join(cities))
    
    cursor.close()
    db.close()
