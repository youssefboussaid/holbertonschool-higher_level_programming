#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # sql query string to be executed on the database
    sql = "SELECT * FROM states ORDER BY id"
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    # Now print fetched result
    for row in results:
        print(row)
    cursor.close()
    db.close()
