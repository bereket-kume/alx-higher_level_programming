#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches the one supplied as an argument. The script is safe
from SQL injections.

Usage:
    ./3-my_safe_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM `states`")

    # Fetch and print states whose name matches the supplied argument
    states = cursor.fetchall()
    [print(state) for state in states if state[1] == sys.argv[4]]
