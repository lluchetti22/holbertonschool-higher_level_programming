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
    
    # Executing using precise query extraction syntax
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC"
    )
    cursor.execute(query, (sys.argv,))
    
    # Extract only the city names into a list
    query_rows = cursor.fetchall()
    cities = [row for row in query_rows]
    
    # Print the cities as a comma-separated string exactly as required
    print(", ".join(cities))
    
    cursor.close()
    db.close()
