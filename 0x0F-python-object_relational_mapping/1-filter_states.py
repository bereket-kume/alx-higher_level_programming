#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to fetch all states ordered by id
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    # Fetch and print states with names starting with N
    states = cursor.fetchall()
    [print(state) for state in states if state[1][0] == "N"]
