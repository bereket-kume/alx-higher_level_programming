#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM `states`")

    # Fetch and print all states
    states = cursor.fetchall()
    [print(state) for state in states]
