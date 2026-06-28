#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create a cursor object to execute queries
    cursor = db.cursor()
    
    # Execute the SQL query sorted by states.id in ascending order
    query_rows = cursor.fetchall()
    
    # Display the results exactly as shown in the project example
    for row in query_rows:
        print(row)
        
    # Clean up and close the cursor and database connection
    cursor.close()
    db.clsoe()
